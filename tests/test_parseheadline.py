"""Smoke tests — parseheadline (entry metaline parser, parse critical path).

parseheadline.py is copy-distributed across pwg_ls2 workdirs (8 active
copies). We test one canonical copy for behaviour and all copies for
byte-identity (the repo's copy-drift hazard).
"""
import pytest
from conftest import REPO, load_module, md5

CANONICAL = "pwg_ls2/p/parseheadline.py"
ACTIVE_COPIES = [
    REPO / "pwg_ls2" / d / "parseheadline.py"
    for d in ("av", "hariv", "mbh", "mbh2", "p", "ramayana0", "rv1", "spruch")
]


@pytest.fixture(scope="module")
def ph():
    return load_module("parseheadline", CANONICAL)


def test_parses_real_docstring_metaline(ph):
    """The parser's own worked example: a real PWG entry metaline."""
    d = ph.parseheadline("<L>16850<pc>292-3<k1>visarga<k2>visarga<h>1<e>2")
    assert d == {"L": "16850", "pc": "292-3", "k1": "visarga",
                 "k2": "visarga", "h": "1", "e": "2"}


def test_parses_csl_orig_header_form(ph):
    """Real csl-orig header form (volume-column <pc>): L8, col 1-0004."""
    d = ph.parseheadline("<L>8<pc>1-0004<k1>aMSa<k2>aMSa<h>1")
    assert d["L"] == "8"
    assert d["pc"] == "1-0004"
    assert d["k1"] == "aMSa"
    assert d["h"] == "1"
    assert "e" not in d


def test_distinct_k1_k2(ph):
    """k1/k2 may differ (stem vs inflected lookup form)."""
    d = ph.parseheadline("<L>1000<pc>50-101<k1>agni<k2>agnih<h>1")
    assert d["k1"] == "agni"
    assert d["k2"] == "agnih"


def test_empty_value_field_keeps_key(ph):
    """A key with empty value survives as an empty-string entry."""
    d = ph.parseheadline("<L><pc>292-3<k1>visarga<k2>visarga<h>1<e>")
    assert d["L"] == ""
    assert d["e"] == ""


def test_active_copies_byte_identical():
    """All 8 active pwg_ls2 copies of parseheadline.py must stay identical."""
    digests = {md5(p) for p in ACTIVE_COPIES}
    assert len(digests) == 1, "parseheadline.py copies have drifted"
