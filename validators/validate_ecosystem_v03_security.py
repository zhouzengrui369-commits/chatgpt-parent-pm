#!/usr/bin/env python3
"""Fail-closed v0.3 permission and security validator."""

from __future__ import annotations
import argparse,json,re
from datetime import datetime,timezone
from pathlib import Path
from typing import Any

SHA256=re.compile(r"^[0-9a-f]{64}$")
WRITE_ACTIONS={"PROPOSE_WRITE","ACCEPT_WRITE","EXECUTE","EXPORT","DELETE"}
AUTH_RANK={"NONE":0,"READ_ONLY":1,"PROPOSE_WRITE":2,"ACCEPT_WRITE":3,"EXECUTE":4}
REQUIRED_AUTH={"PROPOSE_WRITE":2,"ACCEPT_WRITE":3,"EXPORT":3,"DELETE":3,"EXECUTE":4}

class SecurityValidationError(ValueError):
 def __init__(self,code:str,path:str):super().__init__(f"{code}:{path}");self.code=code;self.path=path

def require(ok:bool,code:str,path:str)->None:
 if not ok:raise SecurityValidationError(code,path)

def hash_or_none(value:Any)->bool:return value is None or (isinstance(value,str) and SHA256.fullmatch(value) is not None)
def parse_time(value:Any,path:str)->datetime:
 try:return datetime.fromisoformat(str(value).replace("Z","+00:00"))
 except ValueError:raise SecurityValidationError("BLOCKED_TIMESTAMP_INVALID",path)

def validate_record(data:dict[str,Any])->None:
 require(data.get("schema_version")=="1.0.0","BLOCKED_SCHEMA_VERSION_UNSUPPORTED","schema_version")
 require(data.get("record_kind")=="ECOSYSTEM_V03_SECURITY_GRANT","BLOCKED_RECORD_KIND_INVALID","record_kind")
 grant=data.get("grant");request=data.get("request");gates=data.get("owner_gates");sec=data.get("security")
 for name,value in (("grant",grant),("request",request),("owner_gates",gates),("security",sec)):require(isinstance(value,dict),"BLOCKED_REQUIRED_FIELD_MISSING",name)
 evaluation=parse_time(data.get("evaluation_at"),"evaluation_at");expiry=parse_time(grant.get("expires_at"),"grant.expires_at")
 require(expiry>evaluation,"BLOCKED_PERMISSION_GRANT_EXPIRED","grant.expires_at")
 require(grant.get("revocable") is True,"BLOCKED_PERMISSION_SCOPE_UNPROVEN","grant.revocable")
 require(request.get("consumer") in grant.get("consumers",[]),"BLOCKED_PERMISSION_SCOPE_UNPROVEN","request.consumer")
 require(request.get("namespace") in grant.get("namespaces",[]),"BLOCKED_PERMISSION_SCOPE_UNPROVEN","request.namespace")
 require(request.get("action") in grant.get("actions",[]),"BLOCKED_PERMISSION_SCOPE_UNPROVEN","request.action")
 require(request.get("processing_location") in grant.get("processing_locations",[]),"BLOCKED_PERMISSION_SCOPE_UNPROVEN","request.processing_location")
 require(request.get("purpose") in grant.get("purposes",[]),"BLOCKED_COLLECTION_REUSED_FOR_UNDECLARED_PURPOSE","request.purpose")
 data_class=grant.get("data_class")
 require(data_class in {"D0","D1","D2","D3"},"BLOCKED_PERMISSION_SCOPE_UNPROVEN","grant.data_class")
 for field in ("d2_d3_receipt_sha256","e3_plus_receipt_sha256"):require(hash_or_none(gates.get(field)),"BLOCKED_OWNER_GATE_IDENTITY_INVALID","owner_gates."+field)
 for field in ("cloud_egress_receipt_sha256","agent_write_receipt_sha256"):require(hash_or_none(sec.get(field)),"BLOCKED_PERMISSION_RECEIPT_INVALID","security."+field)
 if data_class in {"D2","D3"}:require(gates.get("d2_d3_receipt_sha256") is not None,"BLOCKED_D2_D3_PRODUCT_GATE_MISSING","owner_gates.d2_d3_receipt_sha256")
 if data_class=="D3":require(sec.get("ordinary_index") is False and sec.get("ordinary_log") is False,"BLOCKED_D3_ORDINARY_INDEX_OR_LOG_PATH","security")
 if sec.get("cloud_egress") is True:require(sec.get("cloud_egress_receipt_sha256") is not None and request.get("processing_location") in {"PRIVATE_CLOUD","PUBLIC_CLOUD"},"BLOCKED_CLOUD_EGRESS_AUTHORITY_MISSING","security.cloud_egress_receipt_sha256")
 elif request.get("processing_location")!="LOCAL_DEVICE":raise SecurityValidationError("BLOCKED_CLOUD_EGRESS_AUTHORITY_MISSING","request.processing_location")
 action=request.get("action")
 if action in WRITE_ACTIONS:
  require(AUTH_RANK.get(grant.get("agent_authority"),-1)>=REQUIRED_AUTH[action] and sec.get("agent_write_receipt_sha256") is not None,"BLOCKED_AGENT_WRITE_AUTHORITY_MISSING","grant.agent_authority")
 risk=grant.get("execution_risk")
 if action=="EXECUTE" and risk in {"E3","E4","E5"}:require(gates.get("e3_plus_receipt_sha256") is not None,"BLOCKED_E3_PLUS_OWNER_AUTHORITY_MISSING","owner_gates.e3_plus_receipt_sha256")
 if action=="DELETE":
  life=sec.get("deletion_lifecycle");require(isinstance(life,dict) and life.get("bound") is True and set(life.get("covers",[]))=={"SOURCE","DERIVED_OBJECT","VECTOR","GRAPH","CACHE","BACKUP"},"BLOCKED_DELETION_LIFECYCLE_UNBOUND","security.deletion_lifecycle")
 if action=="EXPORT":
  life=sec.get("export_lifecycle");require(isinstance(life,dict) and life.get("bound") is True and isinstance(life.get("destination"),str),"BLOCKED_EXPORT_LIFECYCLE_UNBOUND","security.export_lifecycle")
 require(sec.get("secret_reference_only") is True,"BLOCKED_SECRET_MATERIAL_INLINE","security.secret_reference_only")
 ceilings=data.get("claim_ceiling");require(isinstance(ceilings,list) and "SCHEMA_FIXTURE_ONLY" in ceilings and "NO_REAL_PERMISSION_GRANTED" in ceilings,"BLOCKED_FIXTURE_CLAIM_ESCALATION","claim_ceiling")

def main()->int:
 p=argparse.ArgumentParser();p.add_argument("record",type=Path);a=p.parse_args()
 try:
  data=json.loads(a.record.read_text(encoding="utf-8"));require(isinstance(data,dict),"BLOCKED_ROOT_TYPE","$");validate_record(data)
 except (OSError,json.JSONDecodeError,SecurityValidationError) as exc:
  out={"status":"FAIL","code":exc.code,"path":exc.path} if isinstance(exc,SecurityValidationError) else {"status":"FAIL","code":type(exc).__name__,"detail":str(exc)}
  print(json.dumps(out,sort_keys=True));return 1
 print(json.dumps({"status":"PASS","grant_id":data["grant"]["grant_id"],"data_class":data["grant"]["data_class"]},sort_keys=True));return 0
if __name__=="__main__":raise SystemExit(main())
