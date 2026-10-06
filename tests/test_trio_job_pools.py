import pathlib
import re

DOC = pathlib.Path("docs/research/trio-job-pools.md")
# ISCO-08 2-digit only: major groups were rejected as too coarse on PR #40
TRIO = r"[A-Z]{2}:[A-Z]{2}:OC\d\d"


def _rows(text):
    return [l for l in text.splitlines() if re.match(rf"\| \d+ \| {TRIO} \|", l)]


def test_launch_set_is_30_ranked_trios():
    text = DOC.read_text(encoding="utf-8")
    section = text.split("LAUNCH SET:", 1)[1].split("\n## ", 1)[0]
    launch = re.findall(rf"^- ({TRIO})$", section, re.M)
    assert len(launch) == 30 and len(set(launch)) == 30
    table = [r.split("|")[2].strip() for r in _rows(text)]
    assert set(launch) <= set(table)
    assert launch == table[:30]


def test_every_row_has_url_and_retrieval_date():
    text = DOC.read_text(encoding="utf-8")
    rows = _rows(text)
    assert len(rows) >= 30
    assert len(re.findall(r"https?://", text)) >= len(rows)
    assert len(re.findall(r"\| \d{4}-\d{2}-\d{2} \|$", text, re.M)) >= len(rows)
