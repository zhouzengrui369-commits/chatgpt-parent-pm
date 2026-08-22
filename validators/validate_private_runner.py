#!/usr/bin/env python3
"""Fail-closed semantic validation for private-repository Runner contracts."""
from __future__ import annotations
import argparse, hashlib, json, re, sys
from pathlib import Path

SHA40=re.compile(r"^[0-9a-f]{40}$")
SHA256=re.compile(r"^[0-9a-f]{64}$")
FALSE_PROFILE={"local_agent_fallback","source_mutation","local_repair","owner_source_write","manual_status_override","production_db_write","cloud_write","predecessor_reuse","broad_process_kill","runner_auto_repair_by_codex","push","merge","deploy","release"}
FALSE_REQUEST={"source_mutation","local_repair","push","merge","cloud_deploy","release","owner_source_write","manual_status_override","production_db_write","broad_process_kill"}
FAILURE_CLASSES={"NONE","TASK_CONTRACT_DEFECT","SOURCE_DEFECT","WORKFLOW_DEFECT","RUNNER_DEFECT","TOOLCHAIN_DEFECT","DATA_POLICY_DEFECT","PII_DEFECT","IMPORT_FIDELITY_DEFECT","RUNTIME_DEFECT","EVIDENCE_INCOMPLETE"}
FORBIDDEN=("killall","pkill -f","git push","git merge","gh pr merge","tcb ","release create")

def load(path:Path): return json.loads(path.read_text(encoding="utf-8"))
def canonical_sha256(obj)->str:
    raw=json.dumps(obj,ensure_ascii=False,sort_keys=True,separators=(",",":")).encode()
    return hashlib.sha256(raw).hexdigest()
def absolute(v)->bool: return isinstance(v,str) and v.startswith("/") and ".." not in Path(v).parts

def validate_profile(p):
    e=[]
    if p.get("schema_version")!="parent-pm.runner-profile.v1":e.append("BLOCKED_RUNNER_PROFILE_SCHEMA_VERSION")
    if p.get("repository_visibility")!="private":e.append("BLOCKED_EXECUTOR_VISIBILITY_POLICY_MISMATCH")
    if p.get("executor")!="MAC_MINI_SELF_HOSTED_RUNNER" or p.get("registration_scope")!="repository":e.append("BLOCKED_PRIVATE_RUNNER_SCOPE")
    repo=str(p.get("repository","")); name=repo.split("/",1)[1] if "/" in repo else ""
    if p.get("repository_scope_id")!=f"{name}_repository":e.append("BLOCKED_RUNNER_REPOSITORY_SCOPE_ID")
    labels=set(p.get("labels") or [])
    if not {"self-hosted","macOS","ARM64",name}.issubset(labels):e.append("BLOCKED_RUNNER_REQUIRED_LABELS")
    service=p.get("service") or {}; paths=p.get("paths") or {}
    if service.get("unique") is not True or paths.get("unique") is not True:e.append("BLOCKED_RUNNER_UNIQUE_SERVICE_WORKDIR")
    for key,val in [("service.root",service.get("root")),("paths.work_dir",paths.get("work_dir")),("paths.task_root",paths.get("task_root")),("paths.evidence_root",paths.get("evidence_root")),("global_mutex.path",(p.get("global_mutex") or {}).get("path")),("protected_resource_registry",p.get("protected_resource_registry"))]:
        if not absolute(val):e.append(f"BLOCKED_RUNNER_ABSOLUTE_PATH:{key}")
    secrets=p.get("secrets") or {}
    if secrets.get("scope")!="repository" or secrets.get("repository_specific") is not True:e.append("BLOCKED_RUNNER_SECRET_SCOPE")
    concurrency=p.get("concurrency") or {}
    if concurrency.get("max_local")!=1 or concurrency.get("global_mac_mutex") is not True:e.append("BLOCKED_RUNNER_CONCURRENCY")
    if (p.get("global_mutex") or {}).get("stale_lock_policy")!="BLOCK_NOT_AUTO_DELETE":e.append("BLOCKED_RUNNER_MUTEX_STALE_POLICY")
    data=p.get("data_policy") or {}
    if data.get("default_class") not in {"D0_SYNTHETIC","D1_SANITIZED","D0_SYNTHETIC_OR_D1_SANITIZED"}:e.append("BLOCKED_RUNNER_DATA_CLASS")
    for k in ("raw_production_pii","d2_default_access","d3_access"):
        if data.get(k) is not False:e.append(f"BLOCKED_RUNNER_DATA_POLICY:{k}")
    net=p.get("network_policy") or {}
    if net.get("mode")!="DENY_BY_DEFAULT" or not isinstance(net.get("allowlist"),list):e.append("BLOCKED_RUNNER_NETWORK_POLICY")
    auth=p.get("authority") or {}
    for k in FALSE_PROFILE:
        if auth.get(k) is not False:e.append(f"BLOCKED_RUNNER_AUTHORITY:{k}")
    codex=p.get("codex") or {}; expected={"engineering_model":"Luna","engineering_reasoning":"xhigh","product_model":"Sol","product_reasoning":"xhigh","silent_fallback":False}
    for k,v in expected.items():
        if codex.get(k)!=v:e.append(f"BLOCKED_CODEX_MODEL_PROFILE:{k}")
    if any(str(v).lower()=="strongest" for v in codex.values()):e.append("BLOCKED_CODEX_STRONGEST_CONTRACT_VALUE")
    return e

def validate_request(r,p):
    e=[]
    if r.get("schema_version")!="parent-pm.local-execution-request.v1":e.append("BLOCKED_RUNNER_REQUEST_SCHEMA_VERSION")
    if r.get("repository")!=p.get("repository"):e.append("BLOCKED_RUNNER_REQUEST_REPOSITORY")
    for k in ("candidate_sha","candidate_tree","framework_sha"):
        if not SHA40.fullmatch(str(r.get(k,""))):e.append(f"BLOCKED_RUNNER_REQUEST_SHA:{k}")
    if r.get("runner_profile_sha256")!=canonical_sha256(p):e.append("BLOCKED_RUNNER_PROFILE_HASH")
    script=str(r.get("task_script",""))
    if not script.startswith("work/tasks/") or ".." in Path(script).parts:e.append("BLOCKED_RUNNER_TASK_SCRIPT")
    fresh=r.get("freshness") or {}
    for k in ("worktree","task_root","evidence_root","release","runtime"):
        if fresh.get(k) is not True:e.append(f"BLOCKED_PREDECESSOR_REUSE_FRESHNESS:{k}")
    if fresh.get("predecessor_reuse") is not False:e.append("BLOCKED_PREDECESSOR_REUSE")
    if r.get("data_class") not in {"D0_SYNTHETIC","D1_SANITIZED","D0_SYNTHETIC_OR_D1_SANITIZED"}:e.append("BLOCKED_RUNNER_DATA_CLASS")
    auth=r.get("authority") or {}
    for k in FALSE_REQUEST:
        if auth.get(k) is not False:e.append(f"BLOCKED_RUNNER_REQUEST_AUTHORITY:{k}")
    text=json.dumps(r,ensure_ascii=False).lower()
    for token in FORBIDDEN:
        if token in text:e.append(f"BLOCKED_RUNNER_FORBIDDEN_COMMAND:{token}")
    if not r.get("claim_ceiling"):e.append("BLOCKED_RUNNER_CLAIM_CEILING")
    return e

def validate_health(h,p):
    e=[]
    if h.get("schema_version")!="parent-pm.runner-health-receipt.v1":e.append("BLOCKED_RUNNER_HEALTH_SCHEMA_VERSION")
    if h.get("repository")!=p.get("repository") or h.get("repository_scope_id")!=p.get("repository_scope_id"):e.append("BLOCKED_RUNNER_HEALTH_IDENTITY")
    if h.get("service_name")!=(p.get("service") or {}).get("name") or h.get("work_dir")!=(p.get("paths") or {}).get("work_dir"):e.append("BLOCKED_RUNNER_HEALTH_SERVICE")
    if h.get("runner_os")!="macOS" or str(h.get("runner_arch","")).lower()!="arm64":e.append("BLOCKED_RUNNER_HEALTH_PLATFORM")
    if not set(p.get("labels") or []).issubset(set(h.get("labels") or [])):e.append("BLOCKED_RUNNER_HEALTH_LABELS")
    if h.get("health_state")!="HEALTHY" or not str(h.get("runner_version","")).strip():e.append("BLOCKED_RUNNER_UNHEALTHY")
    return e

def validate_receipt(x,r):
    e=[]
    if x.get("schema_version")!="parent-pm.runner-execution-receipt.v1":e.append("BLOCKED_RUNNER_RECEIPT_SCHEMA_VERSION")
    for k in ("request_id","attempt_id","repository","candidate_sha","candidate_tree","runner_profile_sha256"):
        if x.get(k)!=r.get(k):e.append(f"BLOCKED_RUNNER_RECEIPT_BINDING:{k}")
    if x.get("first_blocker") not in FAILURE_CLASSES:e.append("BLOCKED_RUNNER_FIRST_BLOCKER_ENUM")
    if x.get("verdict")=="PASS" and x.get("first_blocker")!="NONE":e.append("BLOCKED_RUNNER_PASS_WITH_BLOCKER")
    clean=x.get("source_clean") or {}
    if clean.get("pre") is not True or clean.get("post") is not True:e.append("BLOCKED_RUNNER_SOURCE_DIRTY")
    prohibited=("source_change","test_change","workflow_change","lockfile_change","git_commit","git_push","owner_source_write","manual_status_override","production_db_write","cloud_write","merge","deploy","release","predecessor_reuse")
    counters=x.get("mutation_counters") or {}
    for k in prohibited:
        if int(counters.get(k,0) or 0)!=0:e.append(f"BLOCKED_RUNNER_PROHIBITED_MUTATION:{k}")
    if x.get("verdict")=="PASS" and not x.get("artifacts"):e.append("BLOCKED_RUNNER_PASS_WITHOUT_ARTIFACTS")
    for a in x.get("artifacts") or []:
        if not SHA256.fullmatch(str(a.get("sha256",""))):e.append("BLOCKED_RUNNER_ARTIFACT_HASH")
    return e

def validate_workflow(path):
    text=Path(path).read_text(encoding="utf-8"); e=[]
    if "workflow_dispatch:" not in text:e.append("BLOCKED_RUNNER_WORKFLOW_NOT_DISPATCH_ONLY")
    if "permissions:\n  contents: read" not in text:e.append("BLOCKED_RUNNER_WORKFLOW_PERMISSIONS")
    if re.search(r"(?mi)^\s*runs-on:\s*['\"]?(?:ubuntu-|windows-|macos-)",text):e.append("BLOCKED_PRIVATE_RUNNER_GITHUB_HOSTED_DEPENDENCY")
    if "actions/upload-artifact@" in text:e.append("BLOCKED_PRIVATE_RUNNER_GITHUB_ARTIFACT_STORAGE_DEPENDENCY")
    for m in re.finditer(r"uses:\s*([^@\s]+)@([^\s]+)",text):
        if not SHA40.fullmatch(m.group(2).strip("'\"")):e.append(f"BLOCKED_RUNNER_ACTION_NOT_FULL_SHA:{m.group(1)}")
    if "runs-on: [self-hosted, macOS, ARM64, __REPOSITORY_LABEL__]" not in text:e.append("BLOCKED_RUNNER_WORKFLOW_LABEL_SCOPE")
    low=text.lower()
    for token in FORBIDDEN:
        if token in low:e.append(f"BLOCKED_RUNNER_WORKFLOW_FORBIDDEN:{token}")
    return e

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--profile",type=Path);ap.add_argument("--request",type=Path);ap.add_argument("--health",type=Path);ap.add_argument("--receipt",type=Path);ap.add_argument("--workflow",type=Path);a=ap.parse_args()
    errors=[];p=r=None
    try:
        if a.profile:p=load(a.profile);errors+=validate_profile(p)
        if a.request:
            if p is None:raise ValueError("--request requires --profile")
            r=load(a.request);errors+=validate_request(r,p)
        if a.health:
            if p is None:raise ValueError("--health requires --profile")
            errors+=validate_health(load(a.health),p)
        if a.receipt:
            if r is None:raise ValueError("--receipt requires --request")
            errors+=validate_receipt(load(a.receipt),r)
        if a.workflow:errors+=validate_workflow(a.workflow)
    except (OSError,json.JSONDecodeError,ValueError) as exc:errors.append(f"BLOCKED_RUNNER_VALIDATOR_INPUT:{exc}")
    if errors:
        print("PRIVATE_RUNNER_CONTRACT: FAIL");[print(f"- {x}") for x in errors];return 1
    print("PRIVATE_RUNNER_CONTRACT: PASS")
    if p is not None:print("RUNNER_PROFILE_SHA256="+canonical_sha256(p))
    return 0
if __name__=="__main__":raise SystemExit(main())
