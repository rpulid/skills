from conftest import discover_top_level_skill_files


def _frontmatter(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    assert lines and lines[0].strip() == "---", f"Missing opening YAML header: {path}"
    closing = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            closing = i
            break
    assert closing is not None, f"Missing closing YAML header: {path}"
    header = "\n".join(lines[1:closing])
    return header


def test_every_skill_has_yaml_header_with_name_description():
    for path in discover_top_level_skill_files():
        header = _frontmatter(path)
        assert "name:" in header, f"Missing name in {path}"
        assert "description:" in header, f"Missing description in {path}"


def test_skill_names_are_unique():
    names = []
    for path in discover_top_level_skill_files():
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.startswith("name:"):
                names.append(line.split(":", 1)[1].strip().strip('"'))
                break
    assert len(names) == len(set(names)), f"Duplicate skill names: {names}"
