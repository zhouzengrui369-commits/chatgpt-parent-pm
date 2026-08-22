import copy
import unittest
from pathlib import Path
from validators.validate_private_runner import canonical_sha256,validate_health,validate_profile,validate_receipt,validate_request,validate_workflow


def profile():
    auth={k:False for k in ['local_agent_fallback','source_mutation','local_repair','owner_source_write','manual_status_override','production_db_write','cloud_write','predecessor_reuse','broad_process_kill','runner_auto_repair_by_codex','push','merge','deploy','release']}
    return {'schema_version':'parent-pm.runner-profile.v1','repository':'owner/demo-private','repository_visibility':'private','executor':'MAC_MINI_SELF_HOSTED_RUNNER','registration_scope':'repository','repository_scope_id':'demo-private_repository','labels':['self-hosted','macOS','ARM64','demo-private','parent-pm-r1'],'service':{'name':'actions.runner.demo-private.mac-mini-r1','root':'/Users/runner/.github-runners/demo-private','unique':True},'paths':{'work_dir':'/Users/runner/.github-runner-work/demo-private','task_root':'/Users/runner/.parent-pm-tasks/demo-private','evidence_root':'/Users/runner/.parent-pm-evidence/demo-private','unique':True},'secrets':{'scope':'repository','repository_specific':True},'concurrency':{'max_local':1,'global_mac_mutex':True},'global_mutex':{'path':'/Users/Shared/chatgpt-parent-pm/mac-mini-global.lock','stale_lock_policy':'BLOCK_NOT_AUTO_DELETE'},'protected_resource_registry':'/Users/runner/.parent-pm/protected-resources/demo-private.json','data_policy':{'default_class':'D0_SYNTHETIC_OR_D1_SANITIZED','raw_production_pii':False,'d2_default_access':False,'d3_access':False},'network_policy':{'mode':'DENY_BY_DEFAULT','allowlist':['github.com','api.github.com']},'authority':auth,'codex':{'engineering_model':'Luna','engineering_reasoning':'xhigh','product_model':'Sol','product_reasoning':'xhigh','silent_fallback':False}}

def request(p):
    auth={k:False for k in ['source_mutation','local_repair','push','merge','cloud_deploy','release','owner_source_write','manual_status_override','production_db_write','broad_process_kill']}
    return {'schema_version':'parent-pm.local-execution-request.v1','request_id':'REQ-1','attempt_id':'ATT-1','repository':p['repository'],'candidate_sha':'1'*40,'candidate_tree':'2'*40,'framework_sha':'3'*40,'runner_profile_sha256':canonical_sha256(p),'task_script':'work/tasks/demo/run.sh','freshness':{'worktree':True,'task_root':True,'evidence_root':True,'release':True,'runtime':True,'predecessor_reuse':False},'data_class':'D0_SYNTHETIC_OR_D1_SANITIZED','network_allowlist':['github.com'],'path_allowlist':['work/tasks/demo'],'endpoint_allowlist':[],'claim_ceiling':['TECHNICAL_GATE_ONLY'],'authority':auth}

class Tests(unittest.TestCase):
    def test_profile_pass(self): self.assertEqual(validate_profile(profile()),[])
    def test_public_rejected(self):
        p=profile();p['repository_visibility']='public';self.assertIn('BLOCKED_EXECUTOR_VISIBILITY_POLICY_MISMATCH',validate_profile(p))
    def test_fallback_rejected(self):
        p=profile();p['authority']['local_agent_fallback']=True;self.assertTrue(any('local_agent_fallback' in x for x in validate_profile(p)))
    def test_scope_and_labels(self):
        p=profile();p['repository_scope_id']='wrong_repository';p['labels'].remove('demo-private');e=validate_profile(p);self.assertIn('BLOCKED_RUNNER_REPOSITORY_SCOPE_ID',e);self.assertIn('BLOCKED_RUNNER_REQUIRED_LABELS',e)
    def test_strongest_rejected(self):
        p=profile();p['codex']['engineering_model']='strongest';self.assertIn('BLOCKED_CODEX_STRONGEST_CONTRACT_VALUE',validate_profile(p))
    def test_request_pass_and_freshness(self):
        p=profile();r=request(p);self.assertEqual(validate_request(r,p),[]);r['freshness']['worktree']=False;self.assertTrue(any('worktree' in x for x in validate_request(r,p)))
    def test_forbidden_command_rejected(self):
        p=profile();r=request(p);r['notes']='pkill -f server';self.assertTrue(any('pkill -f' in x for x in validate_request(r,p)))
    def test_health_binding(self):
        p=profile();h={'schema_version':'parent-pm.runner-health-receipt.v1','repository':p['repository'],'repository_scope_id':p['repository_scope_id'],'runner_name':'r1','service_name':p['service']['name'],'service_root':p['service']['root'],'work_dir':p['paths']['work_dir'],'runner_os':'macOS','runner_arch':'ARM64','labels':p['labels'],'runner_version':'2.999.0','health_state':'HEALTHY','observed_at':'2026-08-22T00:00:00Z'};self.assertEqual(validate_health(h,p),[]);h['health_state']='UNHEALTHY';self.assertIn('BLOCKED_RUNNER_UNHEALTHY',validate_health(h,p))
    def test_receipt_zero_mutations(self):
        p=profile();r=request(p);c={k:0 for k in ['source_change','test_change','workflow_change','lockfile_change','git_commit','git_push','owner_source_write','manual_status_override','production_db_write','cloud_write','merge','deploy','release','predecessor_reuse']};x={'schema_version':'parent-pm.runner-execution-receipt.v1','request_id':r['request_id'],'attempt_id':r['attempt_id'],'repository':r['repository'],'candidate_sha':r['candidate_sha'],'candidate_tree':r['candidate_tree'],'runner_profile_sha256':r['runner_profile_sha256'],'verdict':'PASS','first_blocker':'NONE','source_clean':{'pre':True,'post':True},'artifacts':[{'path':'evidence.json','sha256':'a'*64}],'gate_results':{},'mutation_counters':c,'observed_at':'2026-08-22T00:00:00Z'};self.assertEqual(validate_receipt(x,r),[]);x['mutation_counters']['git_push']=1;self.assertTrue(any('git_push' in e for e in validate_receipt(x,r)))
    def test_workflow_pins(self):
        p=Path(__file__).resolve().parents[2]/'starter-kit/private-runner/private-runner-technical-gate.yml.template';self.assertEqual(validate_workflow(p),[])

if __name__=='__main__': unittest.main()
