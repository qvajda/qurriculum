"""Two-tier ATS gate (ADR-0001 D-2): checks a generated .docx for readability.

An open-source resume parser is the primary tier; python-docx text
extraction is the backup. The tiers are not equivalent, so which one
produced the verdict is always named in the output, never blurred.
"""

import argparse
import re
import sys
from pathlib import Path

import docx

from qurriculum.generate import load_content

EMAIL_RE = re.compile(r"[\w.+-]+@[\w.-]+\.\w+")
PHONE_RE = re.compile(r"\+\d[\d ]{7,}\d")

REQUIRED_SECTION_HEADINGS = ("Formation", "Expérience professionnelle")


def _required_fields(content: dict) -> list[str]:
    headings = {section["heading"] for section in content["sections"]}
    sections = [h for h in REQUIRED_SECTION_HEADINGS if h in headings]
    return ["name", "email", "phone", *sections]


def _document_lines(path: Path) -> list[str]:
    document = docx.Document(path)
    lines = [p.text for p in document.paragraphs]
    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                lines.append(cell.text)
    return lines


def backup_extract(path: Path) -> dict[str, str]:
    """ADR-0001 D-2 backup tier: python-docx text extraction."""
    lines = _document_lines(path)
    text = "\n".join(lines)
    fields: dict[str, str] = {}
    if lines and lines[0].strip():
        fields["name"] = lines[0].strip()
    email = EMAIL_RE.search(text)
    if email:
        fields["email"] = email.group(0)
    phone = PHONE_RE.search(text)
    if phone:
        fields["phone"] = phone.group(0)
    for heading in REQUIRED_SECTION_HEADINGS:
        if heading in lines:
            fields[heading] = heading
    return fields


def primary_extract(path: Path) -> dict[str, str]:
    """ADR-0001 D-2 primary tier: an open-source resume parser."""
    from pyresparser import ResumeParser  # type: ignore[import-not-found]

    data = ResumeParser(str(path)).get_extracted_data()
    fields: dict[str, str] = {}
    if data.get("name"):
        fields["name"] = data["name"]
    if data.get("email"):
        fields["email"] = data["email"]
    if data.get("mobile_number"):
        fields["phone"] = data["mobile_number"]
    text = "\n".join(_document_lines(path))
    for heading in REQUIRED_SECTION_HEADINGS:
        if heading in text:
            fields[heading] = heading
    return fields


def select_tier(path: Path) -> tuple[str, dict[str, str], str | None]:
    """Try the primary tier; fall back to backup on any failure to run it.

    A missing or failing primary is never silently a green primary: it is
    routed to backup and the reason is returned for printing.
    """
    try:
        return "primary", primary_extract(path), None
    except Exception as exc:  # noqa: BLE001 - any parser failure routes to backup
        reason = f"primary unavailable: {exc}"
        return "backup", backup_extract(path), reason


def check(path: Path) -> int:
    try:
        content = load_content()
        required = _required_fields(content)
        tier, fields, reason = select_tier(path)
    except Exception as exc:  # noqa: BLE001 - file could not be read at all
        print(f"error: could not read {path}: {exc}")
        return 2

    if reason:
        print(f"tier={tier}   # {reason}")
    else:
        print(f"tier={tier}")

    missing = []
    for field in required:
        if fields.get(field):
            print(f"{field}: found")
        else:
            missing.append(field)
            print(f"{field}: missing")

    if missing:
        print(f"FAIL: missing {', '.join(missing)}")
        return 1
    print("PASS")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    sys.exit(check(args.path))


if __name__ == "__main__":
    main()
