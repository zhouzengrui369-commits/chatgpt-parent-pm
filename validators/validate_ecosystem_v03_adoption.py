#!/usr/bin/env python3
"""Fail-closed validator for Parent PM ecosystem v0.3 adoption records."""

from __future__ import annotations
import argparse, json, re
from pathlib import Path
from typing import Any

SHA40=re.compile(r"^[0-9a-f]{40}$")
SHA256=re.compile(r"^[0-9a-f]{64}$")
REPO=re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
CAPABILITIES={"knowledge_object","provenance","ingestion","retrieval","review","permission","agent_access","sync_portability","security","feedback"}
STATES={"QUEUED","ACTIVATED","IMPLEMENTING","CANDIDATE","ACCEPTED","BLOCKED","QUEUED_OPTIONAL","NOT_ACTIVATED_NO_CUSTOMER_VALUE"}
TRANSITIONS={
 "QUEUED":{"ACTIVATED","BLOCKED","QUEUED_OPTIONAL","NOT_ACTIVATED_NO_CUSTOMER_VALUE"},
 "QUEUED_OPTIONAL":{"ACTIVATED","NOT_ACTIVATED_NO_CUSTOMER_VALUE","BLOCKED"},
 "ACTIVATED":{"IMPLEMENTING","BLOCKED"},
 "IMPLEMENTING":{"CANDIDATE","BLOCKED"},
 "CANDIDATE":{"ACCEPTED","IMPLEMENTING","BLOCKED"},
 "BLOCKED":{"ACTIVATED","IMPLEMENTING"},
 "ACCEPTED":set(),"NOT_ACTIVATED_NO_CUSTOMER_VALUE":set(),
}

class AdoptionValidationError(ValueError):
 def __init__(self,code:str,path:str):
  super().__init__(f"{code}:{path}");self.code=code;self.path=path

def require(ok:bool,code:str,path:str)->None:
 if not ok: raise AdoptionValidationError(code,path)

def at(data:dict[str,Any],*path:str)->Any:
 cur:Any=data
 for p in path:
  require(isinstance(cur,dict) and p in cur,"BLOCKED_REQUIRED_FIELD_MISSING",".".join(path));cur=cur[p]
 return cur

def exact_hash(value:Any,pattern:re.Pattern[str],code:str,path:str)->None:
 require(isinstance(value,str) and pattern.fullmatch(value) is not None,code,path)

def validate_transition(previous:str,current:str)->None:
 require(previous in STATES and current in STATES,"BLOCKED_MIGRATION_STATE_UNKNOWN","product.migration_state")
 require(previous==current or current in TRANSITIONS[previous],"BLOCKED_MIGRATION_TRANSITION_INVALID",f"{previous}->{current}")

def validate_record(data:dict[str,Any],*,expected_ecosystem_sha:str|None=None,expected_contract_source:str|None=None,expected_contract_manifest_sha256:str|None=None,expected_contract_schema_sha256:str|None=None,previous_state:str|None=None)->None:
 require(data.get("schema_version")=="1.0.0","BLOCKED_SCHEMA_VERSION_UNSUPPORTED","schema_version")
 require(data.get("record_kind")=="ECOSYSTEM_V03_ADOPTION","BLOCKED_RECORD_KIND_INVALID","record_kind")
 require(data.get("program_id")=="PARENT-PM-ECOSYSTEM-V03-R1","BLOCKED_PROGRAM_ID_INVALID","program_id")
 eco=at(data,"ecosystem"); exact_hash(eco.get("commit"),SHA40,"BLOCKED_ECOSYSTEM_BASELINE_SHA_INVALID","ecosystem.commit")
 if expected_ecosystem_sha: require(eco["commit"]==expected_ecosystem_sha,"BLOCKED_ECOSYSTEM_BASELINE_HASH_MISMATCH","ecosystem.commit")
 exact_hash(eco.get("blueprint_blob_sha"),SHA40,"BLOCKED_ECOSYSTEM_BASELINE_SHA_INVALID","ecosystem.blueprint_blob_sha")
 exact_hash(eco.get("blueprint_sha256"),SHA256,"BLOCKED_ECOSYSTEM_BLUEPRINT_HASH_INVALID","ecosystem.blueprint_sha256")
 require(eco.get("status") in {"PROPOSED","HUMAN_OWNER_ACCEPTED"},"BLOCKED_ECOSYSTEM_BASELINE_STATUS_INVALID","ecosystem.status")
 ske=at(data,"shared_knowledge_engine");contract=ske.get("contract")
 require(isinstance(contract,dict),"BLOCKED_SHARED_CONTRACT_NOT_PINNED","shared_knowledge_engine.contract")
 exact_hash(contract.get("source_commit"),SHA40,"BLOCKED_SHARED_CONTRACT_NOT_PINNED","shared_knowledge_engine.contract.source_commit")
 if expected_contract_source: require(contract["source_commit"]==expected_contract_source,"BLOCKED_SHARED_CONTRACT_SOURCE_MISMATCH","shared_knowledge_engine.contract.source_commit")
 for field in ("contract_manifest_sha256","schema_sha256","positive_fixture_sha256","negative_manifest_sha256","conformance_receipt_sha256"):
  exact_hash(contract.get(field),SHA256,"BLOCKED_SHARED_CONTRACT_HASH_INVALID",f"shared_knowledge_engine.contract.{field}")
 if expected_contract_manifest_sha256: require(contract["contract_manifest_sha256"]==expected_contract_manifest_sha256,"BLOCKED_SHARED_CONTRACT_HASH_MISMATCH","shared_knowledge_engine.contract.contract_manifest_sha256")
 if expected_contract_schema_sha256: require(contract["schema_sha256"]==expected_contract_schema_sha256,"BLOCKED_SHARED_CONTRACT_HASH_MISMATCH","shared_knowledge_engine.contract.schema_sha256")
 caps=ske.get("supported_capabilities");require(isinstance(caps,list) and caps and len(caps)==len(set(caps)) and set(caps)<=CAPABILITIES,"BLOCKED_SHARED_CAPABILITY_NOT_SUPPORTED","shared_knowledge_engine.supported_capabilities")
 product=at(data,"product");require(isinstance(product.get("repository"),str) and REPO.fullmatch(product["repository"]) is not None,"BLOCKED_PRODUCT_REPOSITORY_INVALID","product.repository")
 require(isinstance(product.get("project_pm"),str) and bool(product["project_pm"].strip()),"BLOCKED_PROJECT_PM_ACTIVATION_MISSING","product.project_pm")
 state=product.get("migration_state");require(state in STATES,"BLOCKED_MIGRATION_STATE_UNKNOWN","product.migration_state")
 candidate=product.get("current_candidate_sha");require(candidate is None or (isinstance(candidate,str) and SHA40.fullmatch(candidate) is not None),"BLOCKED_CURRENT_CANDIDATE_IDENTITY_INVALID","product.current_candidate_sha")
 if previous_state is not None: validate_transition(previous_state,state)
 activation=at(data,"activation");expected_activation="PLANNED" if state in {"QUEUED","QUEUED_OPTIONAL","NOT_ACTIVATED_NO_CUSTOMER_VALUE"} else "ACTIVATED"
 require(activation.get("state")==expected_activation,"BLOCKED_PROJECT_PM_ACTIVATION_MISSING","activation.state")
 ceilings=data.get("claim_ceiling");require(isinstance(ceilings,list) and ceilings,"BLOCKED_CLAIM_CEILING_MISSING","claim_ceiling")
 if data.get("fixture") is True: require("SCHEMA_FIXTURE_ONLY" in ceilings and not any("PASS" in x and x!="SCHEMA_FIXTURE_ONLY" for x in ceilings),"BLOCKED_FIXTURE_CLAIM_ESCALATION","claim_ceiling")

def main()->int:
 p=argparse.ArgumentParser();p.add_argument("record",type=Path);p.add_argument("--expected-ecosystem-sha");p.add_argument("--expected-contract-source");p.add_argument("--expected-contract-manifest-sha256");p.add_argument("--expected-contract-schema-sha256");p.add_argument("--previous-state");a=p.parse_args()
 try:
  data=json.loads(a.record.read_text(encoding="utf-8"));require(isinstance(data,dict),"BLOCKED_ROOT_TYPE","$")
  validate_record(data,expected_ecosystem_sha=a.expected_ecosystem_sha,expected_contract_source=a.expected_contract_source,expected_contract_manifest_sha256=a.expected_contract_manifest_sha256,expected_contract_schema_sha256=a.expected_contract_schema_sha256,previous_state=a.previous_state)
 except (OSError,json.JSONDecodeError,AdoptionValidationError) as exc:
  out={"status":"FAIL","code":exc.code,"path":exc.path} if isinstance(exc,AdoptionValidationError) else {"status":"FAIL","code":type(exc).__name__,"detail":str(exc)}
  print(json.dumps(out,sort_keys=True));return 1
 print(json.dumps({"status":"PASS","repository":data["product"]["repository"],"migration_state":data["product"]["migration_state"]},sort_keys=True));return 0
if __name__=="__main__":raise SystemExit(main())
