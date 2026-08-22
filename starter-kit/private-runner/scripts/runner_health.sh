#!/usr/bin/env bash
set -euo pipefail
PROFILE="${RUNNER_PROFILE_PATH:-.github/parent-pm-runner/RUNNER_PROFILE.json}"
OUT="${RUNNER_HEALTH_OUT:-${RUNNER_TEMP:?RUNNER_TEMP required}/parent-pm-runner-health.json}"
python - "$PROFILE" "$OUT" <<'PY'
import datetime,json,os,platform,sys
p=json.load(open(sys.argv[1],encoding='utf-8'))
labels=[x for x in os.environ.get('PARENT_PM_RUNNER_LABELS','').split(',') if x] or p.get('labels',[])
version=os.environ.get('ACTIONS_RUNNER_VERSION') or os.environ.get('RUNNER_VERSION') or 'UNKNOWN'
h={
 'schema_version':'parent-pm.runner-health-receipt.v1',
 'repository':p['repository'],'repository_scope_id':p['repository_scope_id'],
 'runner_name':os.environ.get('RUNNER_NAME','UNKNOWN'),'service_name':p['service']['name'],
 'service_root':p['service']['root'],'work_dir':p['paths']['work_dir'],
 'runner_os':os.environ.get('RUNNER_OS','macOS'),'runner_arch':os.environ.get('RUNNER_ARCH',platform.machine()),
 'labels':labels,'runner_version':version,
 'health_state':'HEALTHY' if version!='UNKNOWN' and os.environ.get('RUNNER_NAME') else 'UNHEALTHY',
 'global_mutex_path':p['global_mutex']['path'],'protected_resource_registry':p['protected_resource_registry'],
 'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat()
}
with open(sys.argv[2],'w',encoding='utf-8') as f: json.dump(h,f,ensure_ascii=False,sort_keys=True,indent=2)
print('RUNNER_HEALTH_RECEIPT='+sys.argv[2]);print('RUNNER_HEALTH_STATE='+h['health_state'])
PY
