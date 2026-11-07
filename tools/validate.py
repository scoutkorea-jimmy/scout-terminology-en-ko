#!/usr/bin/env python3
"""Validate terms.csv against the rules in AGENTS.md. Standard library only.

Usage:  python3 tools/validate.py            (from the repository root)
Exit code 0 = no errors. Warnings do not fail the check.
"""
import csv, io, re, sys, collections

PATH = "terms.csv"
COLUMNS = ["term_id", "bp_id", "term_en", "term_en_variant", "term_ko", "term_ko_variant",
           "type", "scope", "equivalent_ksa_term", "term_fr", "definition_ko", "source",
           "source_status", "bp_updated_at", "verify_status", "verify_note", "verify_source",
           "rationale_ko"]
REQUIRED = ["term_id", "term_en", "term_ko", "type", "scope", "definition_ko",
            "source_status", "verify_status"]
TYPES = {"award", "document", "event", "governance", "initiative", "method", "observance",
         "organization", "rank", "role", "section", "skill", "training", "uniform-symbol"}
VERIFY = {"verified", "partly_verified", "corrected", "edited", "generic_definition",
          "editorial_choice"}
SOURCE = {"cited", "not_required", "compiler"}
SCOPE = re.compile(r"^(international|[A-Z]{2}(;[A-Z]{2})*)$")
ID = re.compile(r"^SKT-\d{4}$")
# Expressions retired by recorded decisions (docs/DECISIONS.md). They may appear only in
# *_variant columns, never as a headword or inside a definition.
RETIRED = ["진보 제도", "세계스카우트사무국", "청소년자문위원", "지역사무국장"]

errors, warnings = [], []
raw = open(PATH, "rb").read()
if not raw.startswith(b"\xef\xbb\xbf"):
    errors.append("terms.csv must be UTF-8 with BOM")
rows = list(csv.reader(io.StringIO(raw.decode("utf-8-sig"))))
if not rows:
    print("ERROR terms.csv is empty")
    sys.exit(1)
if rows[0] != COLUMNS:
    print(f"ERROR header mismatch: {rows[0]}")
    sys.exit(1)
for i, r in enumerate(rows[1:], 2):
    if len(r) != len(rows[0]):
        errors.append(f"line {i}: {len(r)} fields, expected {len(rows[0])}")
if errors:
    for e in errors:
        print("ERROR", e)
    sys.exit(1)
data = [dict(zip(rows[0], r)) for r in rows[1:]]

ids = [d["term_id"] for d in data]
nums = []
for d in data:
    t = d["term_id"]
    if not ID.match(t):
        errors.append(f"{t}: bad term_id format")
    else:
        nums.append(int(t[4:]))
    for k in REQUIRED:
        if not d.get(k, "").strip():
            errors.append(f"{t}: empty {k}")
    for k, v in d.items():
        if v != v.strip() or "\n" in v or "  " in v:
            errors.append(f"{t}: whitespace problem in {k}")
    if d["type"] not in TYPES:
        errors.append(f"{t}: unknown type {d['type']}")
    if not SCOPE.match(d["scope"]):
        errors.append(f"{t}: bad scope {d['scope']}")
    if d["verify_status"] not in VERIFY:
        errors.append(f"{t}: unknown verify_status {d['verify_status']}")
    if d["verify_status"] == "partly_verified":
        warnings.append(f"{t}: partly verified; review verify_note before release")
    if d["source_status"] not in SOURCE:
        errors.append(f"{t}: unknown source_status {d['source_status']}")
    if d["source_status"] == "cited" and not d["source"]:
        errors.append(f"{t}: cited but source is empty")
    if d["verify_status"] == "verified" and not d["verify_source"]:
        errors.append(f"{t}: verified but verify_source is empty")
    if d["verify_status"] == "editorial_choice" and not d["rationale_ko"]:
        errors.append(f"{t}: editorial_choice needs rationale_ko")
    df = d["definition_ko"]
    if re.search(r"(입니다|습니다)", df):
        errors.append(f"{t}: definition must use the plain written style (~이다), not ~입니다")
    if re.search(r"출처\s*[:：]", df):
        errors.append(f"{t}: put sources in the source column, not inside definition_ko")
    for w in RETIRED:
        if w in d["term_ko"] or w in df:
            errors.append(f"{t}: retired expression '{w}' used (see docs/DECISIONS.md)")
    for m in re.findall(r"SKT-\d{4}", " ".join(v for k, v in d.items() if k != "term_id")):
        if m not in ids:
            errors.append(f"{t}: reference to unknown {m}")

c = collections.Counter(ids)
errors += [f"duplicate term_id {k}" for k, v in c.items() if v > 1]
c = collections.Counter(d["term_en"].lower() for d in data)
errors += [f"duplicate term_en {k}" for k, v in c.items() if v > 1]
if nums and nums != sorted(nums):
    errors.append("rows must be ordered by term_id")
if nums and nums[0] != 1:
    warnings.append("first term_id is not SKT-0001")
c = collections.Counter(d["term_ko"] for d in data)
known = {"대표단", "대표단장"}  # documented overlaps (README > Limitations)
for k, v in c.items():
    if v > 1 and k not in known:
        warnings.append(f"term_ko '{k}' is used by {v} headwords; document it or distinguish it")

for w in warnings:
    print("WARN ", w)
for e in errors:
    print("ERROR", e)
print(f"{len(data)} terms, {len(errors)} errors, {len(warnings)} warnings")
sys.exit(1 if errors else 0)
