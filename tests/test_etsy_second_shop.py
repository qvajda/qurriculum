import pathlib
import re

DOC = pathlib.Path("docs/research/etsy-second-shop.md")
VERDICTS = ["ONE ACCOUNT MAY HOLD MULTIPLE SHOPS", "ONE SHOP PER ACCOUNT", "UNSETTLED"]
POLICY_URL = re.compile(
    r"https?://(www\.)?etsy\.com/(legal|seller-handbook)/|https?://help\.etsy\.com/hc/"
)


def _text():
    return DOC.read_text(encoding="utf-8")


def test_exactly_one_verdict_line():
    t = _text()
    found = [v for v in VERDICTS if re.search(rf"^{re.escape(v)}\s*$", t, re.M)]
    assert len(found) == 1, found


def test_only_etsy_policy_sources_with_date_and_quote():
    t = _text()
    urls = re.findall(r"https?://[^\s)\]>`]+", t)
    assert urls, "no source URL"
    bad = [u for u in urls if not POLICY_URL.match(u)]
    assert not bad, bad
    assert re.search(r"\b20\d\d-\d\d-\d\d\b", t), "no retrieval date"
    assert ">" in t, "no quoted clause"


def test_second_account_section_matches_verdict():
    t = _text()
    if re.search(r"^ONE SHOP PER ACCOUNT\s*$", t, re.M):
        assert "## Second account" in t
    else:
        assert "## Second account" not in t


def test_consequence_stated():
    assert "## What this forces" in _text()
