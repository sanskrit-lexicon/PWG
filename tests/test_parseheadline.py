"""Smoke tests: parseheadline.py — the PWG entry-headline parser."""
from conftest import PARSEHEADLINE_COPIES, REAL, REPO, load_module


def test_parses_real_nAraka_header(parseheadline):
    d = parseheadline.parseheadline(REAL["nAraka_header"])
    assert d == {"L": "38493", "pc": "4-0117", "k1": "nAraka", "k2": "nAraka"}


def test_parses_real_header_with_optional_keys(parseheadline):
    d = parseheadline.parseheadline(REAL["aMSa_header"])
    assert d == {"L": "8", "pc": "1-0004", "k1": "aMSa", "k2": "aMSa", "h": "1"}


def test_parses_real_header_with_empty_trailing_value(parseheadline):
    d = parseheadline.parseheadline(REAL["visarga_header"])
    assert d == {
        "L": "16850",
        "pc": "292-3",
        "k1": "visarga",
        "k2": "visarga",
        "h": "1",
        "e": "2",
    }


def test_preserves_slash_in_headword(parseheadline):
    d = parseheadline.parseheadline(REAL["puruza_header"])
    assert d["k1"] == "puruza"
    assert d["k2"] == "pu/ruza"


def test_line_without_keys_yields_empty_dict(parseheadline):
    assert parseheadline.parseheadline("nokeyval") == {}


def test_roundtrip_reconstruction_of_real_headers(parseheadline):
    for header in (REAL["nAraka_header"], REAL["puruza_header"], REAL["aMSa_header"]):
        d = parseheadline.parseheadline(header)
        rebuilt = "".join(f"<{k}>{v}" for k, v in d.items())
        assert rebuilt == header


def test_parseheadline_copies_agree_on_real_headers():
    # mbh / av / ramayana0 carry hand-synced copies; all must parse the real
    # headers identically.
    modules = [
        load_module(rel, name=f"parseheadline_{i}")
        for i, rel in enumerate(PARSEHEADLINE_COPIES)
    ]
    for header in REAL["nAraka_header"], REAL["aMSa_header"], REAL["visarga_header"]:
        results = [m.parseheadline(header) for m in modules]
        assert all(r == results[0] for r in results), header
