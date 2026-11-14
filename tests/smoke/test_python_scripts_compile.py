from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_all_python_skill_scripts_compile():
    failures = []
    for path in (ROOT / "skills").rglob("*.py"):
        try:
            compile(path.read_text(encoding="utf-8"), str(path), "exec")
        except SyntaxError as exc:
            failures.append(f"{path}: {exc}")
    assert not failures, "\n".join(failures)
