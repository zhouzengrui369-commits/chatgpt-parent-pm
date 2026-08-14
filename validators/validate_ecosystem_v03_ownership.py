#!/usr/bin/env python3
"""Fail-closed v0.3 PM ownership and evidence-claim validator."""

from __future__ import annotations
import argparse,json,re
from pathlib import Path
from typing import Any

SHA40=re.compile(r"^[0-9a-f]{40}$");SHA256=re.compile(r"^[0-9a-f]{64}$")
LAYERS=["PLANNING","SOURCE_TEST","FIXTURE","REFERENCE_RUNTIME","CONSUMER_RUNTIME","PRODUCT_EXPERIENCE","HUMAN_OWNER","MERGE","RELEASE"]

class OwnershipValidationError(ValueError):
 def __init__(self,code:str,path:str):super().__init__(f"{code}:{path}");self.code=code;self.path=path

def require(ok:bool,code:str,path:str)->None:
 if not ok:raise OwnershipValidationError(code,path)
def receipt(value:Any)->bool:return isinstance(value,str) and SHA256.fullmatch(value) is not None

def validate_record(data:dict[str,Any])->None:
 require(data.get("schema_version")=="1.0.0","BLOCKED_SCHEMA_VERSION_UNSUPPORTED","schema_version")
 require(data.get("record_kind")=="ECOSYSTEM_V03_OWNERSHIP_CLAIM","BLOCKED_RECORD_KIND_INVALID","record_kind")
 actors=data.get("actors");assignment=data.get("assignment");claim=data.get("claim")
 for name,value in (("actors",actors),("assignment",assignment),("claim",claim)):require(isinstance(value,dict),"BLOCKED_REQUIRED_FIELD_MISSING",name)
 action=assignment.get("requested_action");role=assignment.get("requested_actor_role");actor=assignment.get("requested_actor_id")
 require(assignment.get("current_protected_goal") is not None,"BLOCKED_CURRENT_PROTECTED_GOAL_NOT_DECLARED","assignment.current_protected_goal")
 if action=="IMPLEMENT_SHARED_CAPABILITY":require(role=="CAPABILITY_PM" and actor==actors.get("capability_pm"),"BLOCKED_CAPABILITY_PM_OWNERSHIP_MISMATCH","assignment.requested_actor_role")
 if action in {"IMPLEMENT_CONSUMER_PRODUCT","RUN_LOCAL_DEPLOYMENT"}:
  require(role!="ECOSYSTEM_PM","BLOCKED_ECOSYSTEM_PM_PRODUCT_TAKEOVER","assignment.requested_actor_role")
  require(role=="PROJECT_PM" and actor==actors.get("project_pm"),"BLOCKED_PRODUCT_PM_OWNERSHIP_MISMATCH","assignment.requested_actor_role")
  local=assignment.get("local_goal");require(isinstance(local,dict) and receipt(local.get("activation_receipt_sha256")),"BLOCKED_PROJECT_PM_ACTIVATION_MISSING","assignment.local_goal")
 protected=assignment["current_protected_goal"].get("candidate_sha");target=assignment.get("target_candidate_sha")
 if target is not None:
  require(isinstance(target,str) and SHA40.fullmatch(target) is not None,"BLOCKED_CURRENT_CANDIDATE_IDENTITY_INVALID","assignment.target_candidate_sha")
  require(protected is None or target==protected or assignment.get("candidate_transition_authorized") is True,"BLOCKED_CURRENT_CANDIDATE_MUTATION","assignment.target_candidate_sha")
 layer=claim.get("layer");require(layer in LAYERS,"BLOCKED_CLAIM_LAYER_INVALID","claim.layer")
 if claim.get("planning_only") is True:require(layer=="PLANNING","BLOCKED_PLANNING_ONLY_CLAIM_ESCALATION","claim.layer")
 if layer in {"SOURCE_TEST","REFERENCE_RUNTIME","CONSUMER_RUNTIME","PRODUCT_EXPERIENCE","HUMAN_OWNER","MERGE","RELEASE"}:require(receipt(claim.get("source_receipt_sha256")) or layer=="PLANNING","BLOCKED_SOURCE_RECEIPT_MISSING","claim.source_receipt_sha256")
 if layer in {"REFERENCE_RUNTIME","CONSUMER_RUNTIME","PRODUCT_EXPERIENCE","HUMAN_OWNER","MERGE","RELEASE"}:require(receipt(claim.get("runtime_receipt_sha256")),"BLOCKED_SOURCE_TEST_PRESENTED_AS_RUNTIME","claim.runtime_receipt_sha256")
 if claim.get("fixture_data") is True:require(layer=="FIXTURE","BLOCKED_FIXTURE_PRESENTED_AS_REAL_DATA","claim.layer")
 if layer in {"PRODUCT_EXPERIENCE","HUMAN_OWNER","MERGE","RELEASE"}:require(receipt(claim.get("product_experience_receipt_sha256")) and claim.get("independent_reviewer") is True,"BLOCKED_PRODUCT_EXPERIENCE_RECEIPT_MISSING","claim.product_experience_receipt_sha256")
 if layer in {"HUMAN_OWNER","MERGE","RELEASE"}:require(receipt(claim.get("human_owner_receipt_sha256")),"BLOCKED_HUMAN_OWNER_GATE_MISSING","claim.human_owner_receipt_sha256")
 ceilings=data.get("claim_ceiling");require(isinstance(ceilings,list) and "SCHEMA_FIXTURE_ONLY" in ceilings and "NO_REAL_PRODUCT_CLAIM" in ceilings,"BLOCKED_FIXTURE_CLAIM_ESCALATION","claim_ceiling")

def main()->int:
 p=argparse.ArgumentParser();p.add_argument("record",type=Path);a=p.parse_args()
 try:
  data=json.loads(a.record.read_text(encoding="utf-8"));require(isinstance(data,dict),"BLOCKED_ROOT_TYPE","$");validate_record(data)
 except (OSError,json.JSONDecodeError,OwnershipValidationError) as exc:
  out={"status":"FAIL","code":exc.code,"path":exc.path} if isinstance(exc,OwnershipValidationError) else {"status":"FAIL","code":type(exc).__name__,"detail":str(exc)}
  print(json.dumps(out,sort_keys=True));return 1
 print(json.dumps({"status":"PASS","action":data["assignment"]["requested_action"],"layer":data["claim"]["layer"]},sort_keys=True));return 0
if __name__=="__main__":raise SystemExit(main())
