"""Renders the BE:FR analytics FR core as a .docx from committed YAML content.

Structure and prose both live in content/be_fr_analytics.yml (ADR-0001 D-1);
this module walks whatever sections it is given and carries no section names
or ordering of its own.
"""

import argparse
from pathlib import Path

import docx
import yaml

CONTENT_DIR = Path(__file__).parent / "content"
CONTENT_PATHS = {
    "fr": CONTENT_DIR / "be_fr_analytics.yml",
    "en": CONTENT_DIR / "be_fr_analytics_en.yml",
}
DEFAULT_OUT = Path("out/be-fr-analytics-fr.docx")
DEFAULT_OUT_EN = Path("out/be-fr-analytics-en.docx")


def load_content(locale: str = "fr") -> dict:
    return yaml.safe_load(CONTENT_PATHS[locale].read_text(encoding="utf-8"))


def render(content: dict, out: Path) -> Path:
    document = docx.Document()
    document.add_heading(content["name"], level=0)
    document.add_paragraph(content["title"])
    for line in content["contact"]:
        document.add_paragraph(line)
    for section in content["sections"]:
        document.add_heading(section["heading"], level=1)
        for entry in section["entries"]:
            document.add_paragraph(entry)
    out.parent.mkdir(parents=True, exist_ok=True)
    document.save(out)
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--locale", choices=["fr", "en"], default="fr")
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()
    out = args.out or (DEFAULT_OUT if args.locale == "fr" else DEFAULT_OUT_EN)
    render(load_content(args.locale), out)


if __name__ == "__main__":
    main()
