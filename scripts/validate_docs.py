#!/usr/bin/env python3
"""Check local documentation references and the historical PDF baseline.

This verifies file integrity, not the truth of historical security claims.
"""
import hashlib
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
DOCS = ("README.md", "HISTORICAL-EVIDENCE-ADDENDUM.md", "EVIDENCE-REVIEW-CHECKLIST.md")
REPORT = "blockzag-wordpress-audit.pdf"
# The SHA-256 digest of the preserved, publicly committed four-page report
# verified on 2026-11-11. This is a future-change detector, not provenance proof.
REPORT_SHA256 = "33376bb1218a9625f087ee2c0c17f42677e5bbbf19b0e179dff264c899b8056f"
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def validate(root=ROOT):
    errors = []
    for name in DOCS:
        doc = root / name
        if not doc.is_file():
            errors.append(f"Missing required document: {name}")
            continue
        for link in LINK.findall(doc.read_text(encoding="utf-8")):
            destination = link.split()[0].strip("<>")
            if destination.startswith(("https://", "http://", "mailto:", "#")):
                continue  # External targets are not verified here.
            destination = unquote(destination.split("#", 1)[0].split("?", 1)[0])
            if not destination:
                continue
            target = (doc.parent / destination).resolve()
            if not target.is_relative_to(root.resolve()):
                errors.append(f"{name}: reference escapes repository: {destination}")
            elif not target.is_file():
                errors.append(f"{name}: broken local link: {destination}")

    pdf = root / REPORT
    if not pdf.is_file():
        errors.append(f"Missing historical report: {REPORT}")
    else:
        content = pdf.read_bytes()
        if not content.startswith(b"%PDF-"):
            errors.append(f"{REPORT}: invalid PDF signature")
        actual = hashlib.sha256(content).hexdigest()
        if actual != REPORT_SHA256:
            errors.append(f"{REPORT}: SHA-256 differs from historical baseline")
    return errors


def main():
    errors = validate()
    if errors:
        print("DOCUMENT INTEGRITY CHECK FAILED")
        for error in errors:
            print(" - " + error)
        return 1
    print("DOCUMENT INTEGRITY CHECK PASSED")
    print("Local Markdown links resolve; historical PDF matches 2026-11-11 baseline.")
    print("This does not prove the report's historical security claims.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
