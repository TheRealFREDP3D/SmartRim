# Changelog

All notable changes to SmartRim will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- MIT License
- Gitleaks configuration with allowlist for wiki raw HTML
- Gitleaks pre-commit hook for secret scanning
- Cross-platform shell scripts (install.sh, start-monitor.sh, stop-monitor.sh, start-dashboard.sh)
- CLI entry point (main() function) to smartrim.cli for module invocation
- Streamlit dashboard optional dependency
- Structured logging configuration
- Type hints to key modules (monitor.py, mcp_client.py, config.py)
- Custom exception classes for MCP client and monitor operations
- CHANGELOG.md for tracking project changes
- CONTRIBUTING.md for contribution guidelines

### Changed

- Updated README with cross-platform setup instructions (Windows PowerShell and Linux/macOS bash)
- Updated README to explain RimMolt and link to Steam Workshop
- Removed "Windows/PowerShell-based" limitation from README
- Fixed Python version requirement to 3.11+ (matching pyproject.toml)
- Replaced star imports with explicit imports in monitor.py and dashboard.py
- Removed unused variables (cid, situation_risks, date) to fix lint warnings
- Migrated pytest configuration from pytest.ini to pyproject.toml
- Removed deprecated requirements-dev.txt (using pyproject.toml extras)
- Updated .gitignore to fix reflex actor runtime file ignore rules
- Added python-dotenv and version bounds to dependencies

### Fixed

- High-priority lint issues (F405 star-import warnings, F841 unused variables)
- Fixed .gitignore Streamlit skills paths (backslash to forward slash)
- Fixed .gitignore + prefix artifacts from diff merge

## [0.1.0] - 2026-10-26

### Added

- Initial SmartRim implementation
- MCP client for rimmolt server integration
- Colony monitoring with reflex alerts
- LLM integration for debrief analysis and daily advice
- Wiki caching system for RimWorld mechanics
- Streamlit dashboard for colony visualization
- Persistent snapshots, alerts, and debriefs
- Reflex actor (Layer 2) with whitelisted guarded actions
- Test suite with 186 tests
