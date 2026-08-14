#!/usr/bin/env python3
"""Fail-closed v0.3 architecture-boundary validator."""

from __future__ import annotations
import argparse,json,re
from datetime import date
from pathlib import Path
from typing import Any

SHA256=re.compile(r"^[0-9a-f]{64}$")
CAPS={"knowledge_object","provenance","ingestion","retrieval","review","permission","agent_access","sync_portability","security","feedback"}

class ArchitectureValidationError(ValueError):
 def __init__(self,code:str,path:str):super().__init__(f"{code}:{path}");self.code=code;self.path=path

def require(ok:bool,code:str,path:str)->None:
 if not ok:raise ArchitectureValidationError(code,path)

def validate_record(data:dict[str,Any])->None:
 require(data.get("schema_version")=="1.0.0","BLOCKED_SCHEMA_VERSION_UNSUPPORTED","schema_version")
 require(data.get("record_kind")=="ECOSYSTEM_V03_ARCHITECTURE_BOUNDARY","BLOCKED_RECORD_KIND_INVALID","record_kind")
 product=data.get("product");require(isinstance(product,dict),"BLOCKED_REQUIRED_FIELD_MISSING","product")
 require(product.get("project_role")==product.get("adoption_role"),"BLOCKED_PRODUCT_ROLE_MISMATCH","product.project_role")
 try: evaluation=date.fromisoformat(data["evaluation_date"])
 except (KeyError,TypeError,ValueError):raise ArchitectureValidationError("BLOCKED_EVALUATION_DATE_INVALID","evaluation_date")
 physical=data.get("physical_contract");require(isinstance(physical,dict),"BLOCKED_REQUIRED_FIELD_MISSING","physical_contract")
 require(physical.get("exposes_physical_schema") is False and not physical.get("physical_identifiers"),"BLOCKED_PHYSICAL_SCHEMA_EXPOSED_AS_CONTRACT","physical_contract")
 interfaces=physical.get("public_interfaces");require(isinstance(interfaces,list) and not any(str(x).lower().startswith(("sql:","table:","sqlite:")) for x in interfaces),"BLOCKED_PHYSICAL_SCHEMA_EXPOSED_AS_CONTRACT","physical_contract.public_interfaces")
 deviations=data.get("deviations");require(isinstance(deviations,list),"BLOCKED_REQUIRED_FIELD_MISSING","deviations")
 by_id={}
 for i,adr in enumerate(deviations):
  path=f"deviations[{i}]";require(isinstance(adr,dict) and isinstance(adr.get("id"),str), "BLOCKED_DEVIATION_ADR_INVALID",path)
  require(adr.get("status")=="ACCEPTED","BLOCKED_DEVIATION_ADR_NOT_ACCEPTED",path+".status")
  require(isinstance(adr.get("sha256"),str) and SHA256.fullmatch(adr["sha256"]) is not None,"BLOCKED_DEVIATION_ADR_INVALID",path+".sha256")
  try: expiry=date.fromisoformat(adr["expires_on"])
  except (KeyError,TypeError,ValueError):raise ArchitectureValidationError("BLOCKED_DEVIATION_ADR_INVALID",path+".expires_on")
  require(expiry>=evaluation,"BLOCKED_DEVIATION_ADR_EXPIRED",path+".expires_on")
  for field in ("path","owner","reason","interoperability_plan","migration_plan","security_impact"):
   require(isinstance(adr.get(field),str) and bool(adr[field].strip()),"BLOCKED_DEVIATION_ADR_INVALID",path+"."+field)
  by_id[adr["id"]]=adr
 components=data.get("components");require(isinstance(components,list) and components,"BLOCKED_REQUIRED_FIELD_MISSING","components")
 for i,c in enumerate(components):
  path=f"components[{i}]";require(isinstance(c,dict),"BLOCKED_COMPONENT_INVALID",path)
  responsibility=c.get("responsibility");namespace=c.get("namespace")
  if responsibility=="PRODUCT_POLICY" and c.get("contract_surface") is True:raise ArchitectureValidationError("BLOCKED_PRODUCT_SPECIFIC_POLICY_LEAKED_INTO_SHARED_CONTRACT",path)
  if responsibility=="DOMAIN_EXTENSION" and isinstance(namespace,str) and namespace.startswith(("shared.","core.")):raise ArchitectureValidationError("BLOCKED_DOMAIN_EXTENSION_COLLIDES_WITH_CORE_SCHEMA",path+".namespace")
  if responsibility=="SHARED_CONTRACT_ADAPTER":require(c.get("shared_capability") in CAPS,"BLOCKED_SHARED_CAPABILITY_NOT_SUPPORTED",path+".shared_capability")
  if c.get("canonical_truth") is True and responsibility!="SHARED_CONTRACT_ADAPTER":
   deviation_id=c.get("deviation_id");require(isinstance(deviation_id,str) and deviation_id in by_id,"BLOCKED_DUPLICATE_TRUTH_LAYER_WITHOUT_ADR",path+".deviation_id")
 ceilings=data.get("claim_ceiling");require(isinstance(ceilings,list) and "SCHEMA_FIXTURE_ONLY" in ceilings,"BLOCKED_FIXTURE_CLAIM_ESCALATION","claim_ceiling")

def main()->int:
 p=argparse.ArgumentParser();p.add_argument("record",type=Path);a=p.parse_args()
 try:
  data=json.loads(a.record.read_text(encoding="utf-8"));require(isinstance(data,dict),"BLOCKED_ROOT_TYPE","$");validate_record(data)
 except (OSError,json.JSONDecodeError,ArchitectureValidationError) as exc:
  out={"status":"FAIL","code":exc.code,"path":exc.path} if isinstance(exc,ArchitectureValidationError) else {"status":"FAIL","code":type(exc).__name__,"detail":str(exc)}
  print(json.dumps(out,sort_keys=True));return 1
 print(json.dumps({"status":"PASS","repository":data["product"]["repository"]},sort_keys=True));return 0
if __name__=="__main__":raise SystemExit(main())
