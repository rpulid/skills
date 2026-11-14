import re
from pathlib import Path

from conftest import ROOT, discover_top_level_skill_files


def test_index_row_count_matches_discovered_skills():
    index = (ROOT / "INDEX.md").read_text(encoding="utf-8")
    rows = [line for line in index.splitlines() if re.match(r"^\| skills/", line)]
    assert len(rows) == len(discover_top_level_skill_files()), (
        f"INDEX rows={len(rows)} != discovered skills={len(discover_top_level_skill_files())}"
    )


def test_index_paths_are_unique():
    index = (ROOT / "INDEX.md").read_text(encoding="utf-8")
    rows = [line.split("|")[1].strip() for line in index.splitlines() if re.match(r"^\| skills/", line)]
    assert len(rows) == len(set(rows)), "Duplicate INDEX.md skill paths"
