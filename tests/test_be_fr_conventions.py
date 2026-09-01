import re
import pathlib

DOC = pathlib.Path("docs/research/be-fr-analytics-conventions.md")
CITE = re.compile(r"\[source: https?://\S+, retrieved \d{4}-\d{2}-\d{2}\]")
BE_HOST = re.compile(r"https?://(?:www\.)?[^/\s]*\.be/\S+")
CONCLUSION_KEYS = ("SECTIONS:", "ORDER:", "PAGES:", "PHOTO:", "DATES:", "LOCALNESS:")


def _prose_lines(text):
    fenced = False
    for line in text.splitlines():
        if line.startswith("```"):
            fenced = not fenced
            continue
        if not fenced:
            yield line


def test_file_exists():
    assert DOC.exists()


def test_every_quantitative_claim_is_sourced():
    text = DOC.read_text(encoding="utf-8")
    unsourced = [
        line
        for line in _prose_lines(text)
        if re.search(r"\d", line) and not CITE.search(line)
    ]
    assert unsourced == [], unsourced


def test_minimum_sources_and_belgian_share():
    text = DOC.read_text(encoding="utf-8")
    urls = {m.group(0) for m in re.finditer(r"https?://\S+?(?=,)", text)}
    assert len(urls) >= 5, urls
    be_urls = {u for u in urls if BE_HOST.match(u)}
    assert len(be_urls) >= 3, be_urls


def test_conclusion_lines_present_and_non_empty():
    text = DOC.read_text(encoding="utf-8")
    for key in CONCLUSION_KEYS:
        match = re.search(rf"^- {re.escape(key)}\s*(.+)$", text, flags=re.MULTILINE)
        assert match, f"missing conclusion line for {key}"
        assert match.group(1).strip(), f"empty conclusion line for {key}"
