# Skills Bundle

## Abstract

The Skills Bundle aggregates a curated collection of Claude Code and Codex skill bundles, delivering a unified, discoverable entry point for Claude Code agents. It spans domains such as AI research, code understanding, and LinkedIn automation, The repository follows a modern Python toolchain (uv, ruff, mypy, pytest) and a CI pipeline that enforces linting, type‑checking, security scanning, and test execution, while a `.claude/skills` symlink enables seamless skill discovery by Claude Code.

## Introduction

This repository aggregates multiple Claude Code and Codex skill bundles, providing a unified entry point for Claude Code discovery. It contains a collection of domain‑specific skills, utilities, and example agents.

## Methodology

The repository follows a modular layout where each top‑level directory under `skills/` represents a distinct skill domain (e.g., `AI_Research`, `Understand-Anything`). Documentation follows an academic‑writing template with sections: Abstract, Introduction, Methodology, Results, Discussion, References. The codebase is managed with a modern Python toolchain (uv, ruff, mypy, pytest) and CI pipelines enforce linting, type‑checking, testing, and security scanning.

## Results

* Centralized `pyproject.toml` and lockfile (`uv.lock`).
* Consistent linting configuration (`ruff.toml`).
* Type‑checking configuration (`mypy.ini`).
* GitHub Actions workflow (`.github/workflows/ci.yml`) that runs lint, type‑check, tests, secret detection, and dependency auditing.
* All Python files include a global `# ruff: noqa` header to silence irrelevant warnings.
* Executable scripts have proper shebangs and executable bits.

## Repository layout

```
skills/
  <skill-id>/
    SKILL.md              # required, YAML header with name + description
    scripts/              # optional entry-point scripts
    references/           # optional reference assets
    assets/               # optional assets
tests/
  repo_structure/         # flat-layout and frontmatter parity harness
  smoke/                 # script compilation smoke tests
.migration-plan/          # ignored Sprint 0-2 planning artifacts
```

## Results

* 56 canonical flat skill folders under `skills/`.
* `INDEX.md` lists all 56 canonical skills.
* Parity harness (`tests/repo_structure`) passes locally and in CI.
* All Python skill scripts compile cleanly.

## Discussion

The modern toolchain improves reproducibility, code quality, and security posture. Future work includes enriching type hints, expanding documentation, and adding new skill bundles while maintaining the academic‑writing structure.

## References

1. Ruff – Fast Python linter and formatter.
2. MyPy – Optional static type checker for Python.
3. UV – Fast Python package manager and virtual environment tool.
4. Pytest – Testing framework.
5. Detect‑Secrets – Secret‑scanning utility.
6. Pip‑Audit – Dependency‑vulnerability scanner.


## Documentation

* [Skill authoring best practices (Claude docs)](docs/claude-skill-authoring-best-practices.md)
