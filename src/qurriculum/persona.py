"""Builds a BE:FR analytics CV from a persona of raw facts.

The template owns sections, order and date format, per the conclusion lines
of docs/research/be-fr-analytics-conventions.md and ADR-0001. A persona is
facts only; a copy writer (injectable, so tests never call a model) turns
each fact into entry prose. `render` in generate.py does the .docx.
"""

import argparse
from pathlib import Path
from typing import Callable

import yaml

from qurriculum import generate

# SECTIONS + ORDER conclusion lines; experience and formation are
# reverse-chronological.
HEADINGS = {
    "contact": "Coordonnées",
    "schools": "Formation",
    "employers": "Expérience professionnelle",
    "languages": "Langues",
    "skills": "Compétences informatiques",
    "other": "Divers",
}
DEFAULT_OUT = Path("samples/be-fr-analytics-fr.docx")

CopyWriter = Callable[[str, dict], str]


def plain_writer(kind: str, fact: dict) -> str:
    """Deterministic writer: the facts joined, no model. An LLM writer swaps in here."""
    return ", ".join(str(v) for v in fact.values())


def _month(iso: str | None) -> str:
    # DATES: no sourced numeric-vs-textual format; MM/YYYY per role, start–end.
    if not iso:
        return ""
    year, month = str(iso).split("-")
    return f"{month}/{year}"


def _period(item: dict) -> str:
    return f"{_month(item.get('start'))} – {_month(item.get('end')) or 'présent'}"


def _dated(items: list[dict], kind: str, write: CopyWriter) -> list[str]:
    ordered = sorted(items, key=lambda i: str(i["start"]), reverse=True)
    return [
        f"{_period(i)} : "
        + write(kind, {k: v for k, v in i.items() if k not in ("start", "end")})
        for i in ordered
    ]


def build_content(persona: dict, write: CopyWriter = plain_writer) -> dict:
    entries = {
        "schools": _dated(persona.get("schools", []), "school", write),
        "employers": _dated(persona.get("employers", []), "employer", write),
        "languages": [write("language", l) for l in persona.get("languages", [])],
        "skills": [write("skill", {"skill": s}) for s in persona.get("skills", [])],
        "other": [write("other", {"item": s}) for s in persona.get("other", [])],
    }
    return {
        "name": persona["name"],
        "title": persona["title"],
        "contact": persona["contact"],
        "sections": [
            {"heading": HEADINGS[key], "entries": entries[key]}
            for key in HEADINGS
            if key != "contact" and entries[key]
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("persona", type=Path)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    persona = yaml.safe_load(args.persona.read_text(encoding="utf-8"))
    generate.render(build_content(persona), args.out)


if __name__ == "__main__":
    main()
