#!/usr/bin/env bash
set -euo pipefail
PROFILE="${RUNNER_PROFILE_PATH:-.github/parent-pm-runner/RUNNER_PROFILE.json}"
OUT="${RUNNER_UPDATE_OUT:-${RUNNER_TEMP:?RUNNER_TEMP required}/parent-pm-runner-update.json}"
PREVIOUS="${PREVIOUS_RUNNER_VERSION:-UNKNOWN}"
CURRENT="${ACTIONS_RUNNER_VERSION:-${RUNNER_VERSION:-UNKNOWN}}"
STATE="${RUNNER_UPDATE_STATE:-NO_UPDATE_REQUIRED}"
python - "$PROFILE" "$OUT" "$PREVIOUS" "$CURRENT" "$STATE" <<'PY'
import datetime,json,sys
p=json.load(open(sys.argv[1],encoding='utf-8'))
x={'schema_version':'parent-pm.runner-update-receipt.v1','repository':p['repository'],'service_name':p['service']['name'],'previous_version':sys.argv[3],'current_version':sys.argv[4],'update_state':sys.argv[5],'health_reverified':False,'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
with open(sys.argv[2],'w',encoding='utf-8') as f: json.dump(x,f,ensure_ascii=False,sort_keys=True,indent=2)
print('RUNNER_UPDATE_RECEIPT='+sys.argv[2])
PY
