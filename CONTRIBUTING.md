# Contributing to SmartRim

Thank you for your interest in contributing to SmartRim! This document provides guidelines for contributing to the project.

## Development Setup

### Prerequisites
- Python 3.10 or higher
- A local RimWorld installation with the rimmolt mod running
- Ollama (optional, for LLM features)

### Installation
1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```
4. Copy `.env.example` to `.env` and configure your settings

### Running Tests
```bash
pytest -q
```

### Code Quality
- Run `ruff check` to lint the code
- Run `ruff check --fix` to auto-fix issues
- Maintain test coverage for new features

## Project Structure

```
SmartRim/
├── sidecar/           # Main Python sidecar application
│   ├── config.py      # Configuration and environment variables
│   ├── monitor.py     # Colony monitoring and alerts
│   ├── mcp_client.py  # MCP client for rimmolt integration
│   ├── llm.py         # LLM integration (Ollama/OpenAI/Anthropic)
│   ├── dashboard.py   # Streamlit dashboard
│   └── ...
├── tests/             # Test suite
├── memory/            # Persistent data (snapshots, debriefs, wiki cache)
├── schemas/           # JSON schemas for validation
└── docs/              # Documentation
```

## Contribution Guidelines

### Code Style
- Follow PEP 8 style guidelines
- Use type hints for new functions
- Keep functions focused and single-purpose
- Add docstrings for public functions and classes

### Git Workflow
1. Create a branch for your feature: `git checkout -b feature/your-feature`
2. Make your changes and commit with clear messages
3. Run tests and linting before pushing
4. Open a pull request with a description of your changes

### Commit Messages
Use conventional commit format:
- `feat: add new feature`
- `fix: fix bug`
- `docs: update documentation`
- `refactor: refactor code`
- `test: add tests`

### Testing
- Write tests for new functionality
- Ensure all existing tests pass
- Test edge cases and error conditions

### Documentation
- Update README.md if adding user-facing features
- Update relevant documentation files
- Add comments for complex logic

## Design Principles

1. **Deterministic Monitoring**: Keep reflex monitoring deterministic and fast; use LLM for advisory analysis only
2. **Graceful Degradation**: The system should work without LLM/Ollama; degrade gracefully when unavailable
3. **Persistent Memory**: Maintain lessons-learned and debriefs for long-term learning
4. **Runtime over Source**: Prioritize runtime game state (rimmolt) over static source code for colony decisions

## Questions or Issues?

Feel free to open an issue on GitHub for questions, bug reports, or feature requests.
