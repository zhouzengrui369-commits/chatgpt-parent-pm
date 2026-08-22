#!/usr/bin/env python3
import copy, json, re, sys
from datetime import datetime, timezone
from pathlib import Path

SHA40=re.compile(r'^[0-9a-f]{40}$'); SHA64=re.compile(r'^[0-9a-f]{64}$')
FALSE_PERMS=('source_mutation','local_repair','push','merge','tag','release','provider_change')
ALLOWED_CLAIMS={'EXECUTOR_SOURCE','EXECUTOR_TEST','EXECUTOR_BUILD','EXECUTOR_LOCAL_RUNTIME'}
FAILURE_KINDS={'TASK_CONTRACT_DEFECT','SOURCE_DEFECT','WORKFLOW_DEFECT','RUNNER_DEFECT','TOOLCHAIN_DEFECT','PROCESS_LIFECYCLE_DEFECT','NETWORK_DEFECT','EVIDENCE_DEFECT','PRODUCT_RUNTIME_DEFECT'}
MAX_FRESH_AGE_SECONDS=900
FORBIDDEN_COMMANDS=(re.compile(r'(^|\s)killall(\s|$)',re.I),re.compile(r'(^|\s)pkill\s+-f(\s|$)',re.I),re.compile(r'\bgit\s+(push|merge|tag)\b',re.I),re.compile(r'\bgh\s+(pr\s+merge|release)\b',re.I))

def block(code): return code

def parse_time(value):
    if not isinstance(value,str): raise ValueError(value)
    if value.endswith('Z'): value=value[:-1]+'+00:00'
    dt=datetime.fromisoformat(value)
    if dt.tzinfo is None: dt=dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)

def fresh(now,value):
    try: age=(parse_time(now)-parse_time(value)).total_seconds()
    except Exception: return False
    return 0 <= age <= MAX_FRESH_AGE_SECONDS

def validate_bundle(b):
    try:
        now=b['validation_time']; v=b['visibility']; p=b['profile']; r=b['request']; a=b['attempt']; h=b['health']; u=b['update']; g=b['registry']; m=b['material']
    except (KeyError,TypeError): return block('BLOCKED_RUNNER_FRAMEWORK_RECORD_MISSING')
    repo=v.get('repository_full_name')
    if v.get('visibility')!='private': return block('BLOCKED_PUBLIC_REPOSITORY_SELF_HOSTED_RUNNER')
    if v.get('executor_route')!='MAC_MINI_SELF_HOSTED_RUNNER': return block('BLOCKED_EXECUTOR_VISIBILITY_POLICY_MISMATCH')
    if not fresh(now,v.get('observed_at')): return block('BLOCKED_REPOSITORY_VISIBILITY_RECEIPT_STALE')
    if p.get('repository_full_name')!=repo or p.get('repository_visibility')!='private' or p.get('registration_scope')!='repository': return block('BLOCKED_RUNNER_PROFILE_REPOSITORY_MISMATCH')
    if not all(p.get(k) for k in ('profile_id','service_name','work_dir','repository_secret_scope')) or p.get('repository_secret_scope')!=repo: return block('BLOCKED_RUNNER_PROFILE_IDENTITY_INCOMPLETE')
    labels=set(p.get('labels') or [])
    if len(labels)<4 or not {'self-hosted','macOS','ARM64'}.issubset(labels): return block('BLOCKED_RUNNER_PROFILE_LABELS')
    if p.get('max_concurrent_local_execution')!=1 or p.get('global_mac_mutex_required') is not True: return block('BLOCKED_GLOBAL_MAC_MUTEX_OR_CONCURRENCY')
    perms=p.get('permissions') or {}
    if any(perms.get(k) is not False for k in FALSE_PERMS): return block('BLOCKED_RUNNER_PERMISSION_WIDENING')
    net=p.get('network') or {}; allow=net.get('allowlist') or []
    if net.get('default_policy')!='deny' or any(x in ('*','0.0.0.0/0','::/0') for x in allow): return block('BLOCKED_RUNNER_NETWORK_AUTHORITY')
    pp=p.get('process_policy') or {}
    if pp.get('broad_process_kill') is not False or pp.get('owned_pid_pgid_only') is not True: return block('BLOCKED_BROAD_PROCESS_KILL_POLICY')
    if p.get('predecessor_reuse') is not False: return block('BLOCKED_PREDECESSOR_REUSE')
    if r.get('repository_full_name')!=repo or r.get('profile_id')!=p.get('profile_id'): return block('BLOCKED_RUNNER_REQUEST_PROFILE_MISMATCH')
    if not SHA64.match(str(r.get('profile_sha256',''))): return block('BLOCKED_RUNNER_PROFILE_HASH')
    if not SHA40.match(str(r.get('source_sha',''))) or not SHA40.match(str(r.get('source_tree',''))): return block('BLOCKED_RUNNER_SOURCE_IDENTITY')
    if not SHA64.match(str(r.get('request_sha256',''))) or r.get('fresh_attempt_required') is not True: return block('BLOCKED_RUNNER_REQUEST_IDENTITY')
    commands=r.get('allowed_commands') or []
    if any(pattern.search(cmd) for cmd in commands for pattern in FORBIDDEN_COMMANDS): return block('BLOCKED_RUNNER_FORBIDDEN_COMMAND')
    reqnet=r.get('network_allowlist') or []
    if any(x in ('*','0.0.0.0/0','::/0') for x in reqnet) or not set(reqnet).issubset(set(allow)): return block('BLOCKED_RUNNER_REQUEST_NETWORK_WIDENING')
    claims=set(r.get('claim_ceiling') or [])
    if not claims or not claims.issubset(ALLOWED_CLAIMS): return block('BLOCKED_RUNNER_CLAIM_ESCALATION')
    if r.get('material_manifest_sha256')!=m.get('manifest_sha256'): return block('BLOCKED_MATERIAL_MANIFEST_IDENTITY')
    if r.get('protected_registry_sha256')!=g.get('sha256'): return block('BLOCKED_PROTECTED_RESOURCE_REGISTRY_IDENTITY')
    if m.get('data_class') not in ('D0','D1_SYNTHETIC_OR_SANITIZED') or m.get('use_authorized') is not True or m.get('content_egress') is not False or m.get('local_path_publication') is not False: return block('BLOCKED_MATERIAL_DATA_OR_PRIVACY_AUTHORITY')
    if g.get('repository_full_name')!=repo or g.get('broad_process_kill') is not False or g.get('owned_pid_pgid_only') is not True: return block('BLOCKED_PROTECTED_RESOURCE_POLICY')
    if a.get('request_id')!=r.get('request_id') or a.get('profile_id')!=p.get('profile_id') or a.get('source_sha')!=r.get('source_sha') or a.get('source_tree')!=r.get('source_tree'): return block('BLOCKED_RUNNER_ATTEMPT_IDENTITY')
    if len({a.get('worktree_id'),a.get('task_root_id'),a.get('evidence_root_id')})!=3 or any(not x for x in (a.get('attempt_id'),a.get('worktree_id'),a.get('task_root_id'),a.get('evidence_root_id'))): return block('BLOCKED_RUNNER_ATTEMPT_FRESH_IDENTITIES')
    if h.get('profile_id')!=p.get('profile_id') or h.get('repository_full_name')!=repo or h.get('service_name')!=p.get('service_name') or h.get('work_dir')!=p.get('work_dir'): return block('BLOCKED_RUNNER_HEALTH_IDENTITY')
    if not fresh(now,h.get('observed_at')): return block('BLOCKED_RUNNER_HEALTH_STALE')
    if h.get('online') is not True or h.get('global_mutex_available') is not True or h.get('arch')!='arm64' or h.get('os')!='macOS': return block('BLOCKED_RUNNER_HEALTH')
    if u.get('profile_id')!=p.get('profile_id') or u.get('runner_version')!=h.get('runner_version'): return block('BLOCKED_RUNNER_UPDATE_IDENTITY')
    if not fresh(now,u.get('observed_at')): return block('BLOCKED_RUNNER_UPDATE_STALE')
    if u.get('update_state') not in ('CURRENT','UPDATED') or (u.get('update_required') is True and u.get('update_state')!='UPDATED'): return block('BLOCKED_RUNNER_UPDATE_STATE')
    rec=b.get('receipt')
    if rec is not None:
        if rec.get('request_id')!=r.get('request_id') or rec.get('attempt_id')!=a.get('attempt_id') or rec.get('profile_id')!=p.get('profile_id') or rec.get('repository_full_name')!=repo or rec.get('source_sha')!=r.get('source_sha') or rec.get('source_tree')!=r.get('source_tree'): return block('BLOCKED_RUNNER_RECEIPT_IDENTITY')
        if rec.get('source_mutation') is not False or rec.get('local_repair') is not False or rec.get('predecessor_reuse') is not False: return block('BLOCKED_RUNNER_RECEIPT_POLICY_VIOLATION')
        if rec.get('owned_processes_terminal') is not True or rec.get('owned_ports_terminal') is not True: return block('BLOCKED_RUNNER_PROCESS_OR_PORT_NOT_TERMINAL')
        if rec.get('claim_layer')!='EXECUTOR_LOCAL_RUNTIME': return block('BLOCKED_RUNNER_CLAIM_ESCALATION')
        status=rec.get('status'); fc=rec.get('failure_classification')
        if status=='PASS':
            if rec.get('first_blocker') is not None or fc is not None or not rec.get('artifacts'): return block('BLOCKED_RUNNER_PASS_RECEIPT_INCONSISTENT')
        elif status in ('FAIL','BLOCKED'):
            if not rec.get('first_blocker') or not isinstance(fc,dict) or fc.get('kind') not in FAILURE_KINDS: return block('BLOCKED_RUNNER_FAILURE_CLASSIFICATION_MISSING')
        if a.get('state')!=status: return block('BLOCKED_RUNNER_ATTEMPT_RECEIPT_STATE_MISMATCH')
    return None

def load(path): return json.loads(Path(path).read_text())
def set_path(obj,path,value):
    cur=obj; parts=path.split('.')
    for part in parts[:-1]: cur=cur[part]
    cur[parts[-1]]=value

def self_test(root):
    positive=load(root/'fixtures/private-runner/positive-lingxi-shaped.json')
    err=validate_bundle(positive)
    if err: raise SystemExit(f'positive failed: {err}')
    cases=load(root/'fixtures/private-runner/negative-cases.json')
    for case in cases:
        sample=copy.deepcopy(positive); set_path(sample,case['path'],case['value']); actual=validate_bundle(sample)
        if actual!=case['expected_blocker']: raise SystemExit(f"{case['name']}: expected {case['expected_blocker']} got {actual}")
    print(f'PASS_PRIVATE_RUNNER_FRAMEWORK_SELF_TEST positive=1 negative={len(cases)}')

def main():
    root=Path(__file__).resolve().parents[1]
    if len(sys.argv)==2 and sys.argv[1]=='--self-test': self_test(root); return
    if len(sys.argv)!=2: raise SystemExit('usage: validate_private_runner_framework.py <bundle.json>|--self-test')
    err=validate_bundle(load(sys.argv[1]))
    if err: print(err); raise SystemExit(2)
    print('PASS_PRIVATE_RUNNER_FRAMEWORK_VALIDATION')
if __name__=='__main__': main()
