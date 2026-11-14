import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SKILLS_ROOT = ROOT / "skills"


def discover_top_level_skill_files() -> list[Path]:
    """Return only direct children: skills/<id>/SKILL.md."""
    found: list[Path] = []
    if not SKILLS_ROOT.exists():
        return found
    for child in SKILLS_ROOT.iterdir():
        skill_file = child / "SKILL.md"
        try:
            if skill_file.is_file():
                found.append(skill_file)
        except OSError:
            continue
    return sorted(found)
