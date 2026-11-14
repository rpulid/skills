from pathlib import Path

from conftest import ROOT, SKILLS_ROOT, discover_top_level_skill_files

FORBIDDEN_NAMES = {".git", "venv", "node_modules", ".codex-marketplace", ".claude", ".github", ".agents"}


def test_skills_root_exists():
    assert SKILLS_ROOT.exists(), "Missing top-level skills/ directory"


def test_every_skill_is_one_level_deep():
    files = discover_top_level_skill_files()
    assert files, "No top-level SKILL.md files found"
    for path in files:
        rel = path.relative_to(ROOT)
        parts = rel.parts
        assert len(parts) == 3, f"Skill is not flat: {rel}"
        assert parts[0] == "skills"


def test_no_nested_skills_directory():
    for path in discover_top_level_skill_files():
        nested = path.parent / "skills"
        assert not nested.exists(), f"Nested skills directory found: {nested}"


def test_no_vendored_or_hidden_trees_under_skills():
    if not SKILLS_ROOT.exists():
        return
    for child in SKILLS_ROOT.iterdir():
        assert child.name not in FORBIDDEN_NAMES, f"Forbidden top-level entry: {child}"
        for forbidden in FORBIDDEN_NAMES:
            assert not (child / forbidden).exists(), f"Forbidden nested tree: {child / forbidden}"
