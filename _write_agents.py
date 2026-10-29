part1 = r"""# AGENTS.md — SmartRim

This file helps AI agents (and humans) understand how to work with the **SmartRim** project.

SmartRim is an autonomous **RimWorld sidecar**: it observes colony state over the RimMolt MCP server, keeps a persistent lesson store, and advises (or pauses) on threats.

---

## 1. Project at a glance

| Item | Detail |
|------|--------|
| Language | Python 3.11+ |
| Package layout | src/ layout (src/smartrim/) |
| Packaging | pyproject.toml (setuptools), installable with pip install -e ".[dev]" |
| Linter | Ruff (ruff.toml), target py313, line-length 100 |
| Test runner | pytest (python -m pytest or pytest -q), unittest-style TestCase |
| Dependency mgmt | pip + project venv (.venv/) |
| MCP server | RimMolt mod for RimWorld, HTTP API on localhost:8787 (configurable MCP_URL) |
| LLM | Ollama by default (optional; degrades gracefully); OpenAI/Anthropic optional extras |
| Docs | README.md, CONTRIBUTING.md, CHANGELOG.md, memory/*.md, docs/ |

No package.json, no Node.js tooling. Do not run npm.

"""
