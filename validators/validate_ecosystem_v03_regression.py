#!/usr/bin/env python3
"""Umbrella deterministic regression for Parent PM ecosystem v0.3."""

from __future__ import annotations
import argparse,hashlib,json,sys
from pathlib import Path
from typing import Any

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
 sys.path.insert(0,str(ROOT))

from validators.validate_v03_g0_snapshot import validate_snapshot
from validators.validate_ecosystem_v03_adoption import validate_record as validate_adoption
from validators.validate_ecosystem_v03_architecture import validate_record as validate_architecture
from validators.validate_ecosystem_v03_security import validate_record as validate_security
from validators.validate_ecosystem_v03_ownership import validate_record as validate_ownership
from validators.validate_ecosystem_v03_starter_kit import validate_manifest as validate_starter

EXPECTED_COUNTS={"adoption_positive":5,"adoption_negative":5,"architecture_positive":3,"architecture_negative":6,"security_positive":5,"security_negative":9,"ownership_positive":6,"ownership_negative":10,"starter_templates":7}

class RegressionValidationError(ValueError):
 def __init__(self,code:str,path:str):super().__init__(f"{code}:{path}");self.code=code;self.path=path

def require(ok:bool,code:str,path:str)->None:
 if not ok:raise RegressionValidationError(code,path)
def git_blob_sha(path:Path)->str:
 data=path.read_bytes();return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()
def load(path:Path)->dict[str,Any]:return json.loads(path.read_text(encoding="utf-8"))

def validate_release_candidate(manifest_path:Path)->dict[str,int]:
 data=load(manifest_path)
 require(data.get("schema_version")=="1.0.0","BLOCKED_RELEASE_MANIFEST_VERSION","schema_version")
 require(data.get("state")=="CANDIDATE_NOT_RELEASED","BLOCKED_PREMATURE_RELEASE_CLAIM","state")
 require(data.get("protected_base_head")=="93356868f656384c5023bd9db666c73a8524d224","BLOCKED_PROTECTED_BASE_DRIFT","protected_base_head")
 require(data.get("fixture_counts")==EXPECTED_COUNTS,"BLOCKED_REGRESSION_COUNT_DRIFT","fixture_counts")
 for entry in data.get("sources",[]):
  path=ROOT/entry["path"];require(path.is_file() and not path.is_symlink(),"BLOCKED_RELEASE_SOURCE_MISSING",entry["path"])
  require(git_blob_sha(path)==entry["git_blob_sha"],"BLOCKED_RELEASE_SOURCE_BLOB_MISMATCH",entry["path"])

 snapshot=load(ROOT/"work/tasks/2026-08-14-parent-pm-v03-g0-activation/CURRENT_TRUTH_SNAPSHOT.json")
 validate_snapshot(snapshot,expected_main_sha="99e88020789603f17de715775b455e91e4e20b17",expected_protected_head="93356868f656384c5023bd9db666c73a8524d224")
 for path in sorted((ROOT/"fixtures/ecosystem-v03/positive").glob("*.json")):
  validate_adoption(load(path),expected_ecosystem_sha="e46c4be501c465884486a4417adca2e158a58ccc",expected_contract_source="ded00acf02d7714d36c4bcb73b132cb3defdaf09",expected_contract_manifest_sha256="15b989f37028682ca7e1a07e6061f7ebf03eff30c1c5d7a5c4bec90c5326056a",expected_contract_schema_sha256="0e21d3e9f8c07586f4ee896376885ccc27bc7250cb2351f3ab5bec3b87e05324")
 for path in sorted((ROOT/"fixtures/ecosystem-v03/architecture/positive").glob("*.json")):validate_architecture(load(path))
 for path in sorted((ROOT/"fixtures/ecosystem-v03/security/positive").glob("*.json")):validate_security(load(path))
 for path in sorted((ROOT/"fixtures/ecosystem-v03/ownership/positive").glob("*.json")):validate_ownership(load(path))
 validate_starter(ROOT/"starter-kit/ecosystem-v03/template-manifest.json")
 for gate,task in {"G0":"2026-08-14-parent-pm-v03-g0-activation","G1":"2026-08-14-parent-pm-v03-g1-adoption-schema","G2":"2026-08-14-parent-pm-v03-g2-architecture-boundary","G3":"2026-08-14-parent-pm-v03-g3-permission-security","G4":"2026-08-14-parent-pm-v03-g4-ownership-claims","G5":"2026-08-14-parent-pm-v03-g5-starter-kit"}.items():
  text=(ROOT/"work/tasks"/task/"RESULT.md").read_text(encoding="utf-8");require("STATUS=PASS_" in text,"BLOCKED_PRIOR_GATE_RECEIPT_NOT_PASS",gate)
 return EXPECTED_COUNTS

def main()->int:
 p=argparse.ArgumentParser();p.add_argument("manifest",type=Path);a=p.parse_args()
 try:counts=validate_release_candidate(a.manifest)
 except (OSError,json.JSONDecodeError,ValueError) as exc:
  out={"status":"FAIL","code":exc.code,"path":exc.path} if isinstance(exc,RegressionValidationError) else {"status":"FAIL","code":type(exc).__name__,"detail":str(exc)}
  print(json.dumps(out,sort_keys=True));return 1
 print(json.dumps({"status":"PASS","candidate":"0.3.0-rc.1","counts":counts},sort_keys=True));return 0
if __name__=="__main__":raise SystemExit(main())
