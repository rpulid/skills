from pathlib import Path

from conftest import ROOT


def test_gitignore_contains_plan_directory():
    gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
    assert ".migration-plan" in gitignore


def test_gitignore_contains_common_cache_patterns():
    gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
    for pattern in ("__pycache__/", "*.pyc", ".ruff_cache", ".mypy_cache"):
        assert pattern in gitignore, f"Missing ignore pattern: {pattern}"
