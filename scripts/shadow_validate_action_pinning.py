#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github" / "workflows"
USE_RE = re.compile(r"^\s*-?\s*uses:\s*([^\s#]+)")
SHA_RE = re.compile(r"^[0-9a-fA-F]{40}$")

issues = []
for path in sorted(WORKFLOWS.glob("*.y*ml")):
    for lineno, line in enumerate(path.read_text().splitlines(), 1):
        match = USE_RE.match(line)
        if not match:
            continue
        ref = match.group(1)
        if ref.startswith("./"):
            continue
        if "@" not in ref:
            issues.append((path.name, lineno, ref, "ACTION_REF_MISSING"))
            continue
        action, version = ref.rsplit("@", 1)
        if not SHA_RE.fullmatch(version):
            issues.append((path.name, lineno, ref, "UNPINNED_ACTION_REFERENCE"))

for filename, line, ref, code in issues:
    print(f"SHADOW_POLICY {code} {filename}:{line} {ref}")

print(f"SHADOW_ACTION_PINNING issues={len(issues)} blocking=false")
print("SHADOW_ACTION_PINNING=PASS_REPORT_ONLY")
