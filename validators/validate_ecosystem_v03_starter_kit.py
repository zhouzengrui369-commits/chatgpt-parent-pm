#!/usr/bin/env python3
"""Validate completeness and safety of the ecosystem v0.3 starter kit."""

from __future__ import annotations
import argparse,json,re
from pathlib import Path
from typing import Any

PLACEHOLDER=re.compile(r"\{\{[A-Z0-9_]+\}\}")
EXPECTED={
 "ECOSYSTEM_V03_ADOPTION.json.template","CURRENT_TRUTH_SNAPSHOT.md.template","PLANNING_PR.md.template",
 "ACTIVE_GOAL.md.template","CONFORMANCE_EVIDENCE_MANIFEST.json.template","DEVIATION_ADR.md.template","CROSS_PROJECT_TRACKER.json.template"
}
FORBIDDEN=("refs/heads/","/Users/","gho_","github_pat_","sk-")

class StarterKitValidationError(ValueError):
 def __init__(self,code:str,path:str):super().__init__(f"{code}:{path}");self.code=code;self.path=path

def require(ok:bool,code:str,path:str)->None:
 if not ok:raise StarterKitValidationError(code,path)

def validate_template_text(path:str,text:str,required:list[str])->None:
 for placeholder in required:require(placeholder in text,"BLOCKED_STARTER_TEMPLATE_PLACEHOLDER_MISSING",path+":"+placeholder)
 require("latest" not in text.lower(),"BLOCKED_MOVING_REF_FORBIDDEN",path)
 require(not any(token in text for token in FORBIDDEN),"BLOCKED_STARTER_TEMPLATE_UNSAFE_CONTENT",path)
 found=PLACEHOLDER.findall(text);require(bool(found),"BLOCKED_STARTER_TEMPLATE_PLACEHOLDER_MISSING",path)

def validate_manifest(manifest_path:Path)->None:
 data=json.loads(manifest_path.read_text(encoding="utf-8"))
 require(data.get("schema_version")=="1.0.0","BLOCKED_SCHEMA_VERSION_UNSUPPORTED","schema_version")
 entries=data.get("templates");require(isinstance(entries,list) and data.get("template_count")==7 and len(entries)==7,"BLOCKED_STARTER_KIT_INCOMPLETE","templates")
 names={Path(x.get("path","")).name for x in entries if isinstance(x,dict)};require(names==EXPECTED,"BLOCKED_STARTER_KIT_INCOMPLETE","templates")
 root=manifest_path.resolve().parents[2]
 for entry in entries:
  path=Path(entry["path"]);full=root/path
  require(full.is_file() and not full.is_symlink(),"BLOCKED_STARTER_TEMPLATE_MISSING",entry["path"])
  required=entry.get("required_placeholders");require(isinstance(required,list) and required,"BLOCKED_STARTER_TEMPLATE_PLACEHOLDER_MISSING",entry["path"])
  validate_template_text(entry["path"],full.read_text(encoding="utf-8"),required)

def main()->int:
 p=argparse.ArgumentParser();p.add_argument("manifest",type=Path);a=p.parse_args()
 try:validate_manifest(a.manifest)
 except (OSError,json.JSONDecodeError,StarterKitValidationError) as exc:
  out={"status":"FAIL","code":exc.code,"path":exc.path} if isinstance(exc,StarterKitValidationError) else {"status":"FAIL","code":type(exc).__name__,"detail":str(exc)}
  print(json.dumps(out,sort_keys=True));return 1
 print(json.dumps({"status":"PASS","template_count":7},sort_keys=True));return 0
if __name__=="__main__":raise SystemExit(main())
