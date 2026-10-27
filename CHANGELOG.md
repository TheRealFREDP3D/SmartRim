# Changelog

All notable changes to SmartRim will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Structured logging configuration
- Type hints to key modules (monitor.py, mcp_client.py, config.py)
- Custom exception classes for MCP client and monitor operations
- CHANGELOG.md for tracking project changes
- CONTRIBUTING.md for contribution guidelines

### Changed
- Replaced star imports with explicit imports in monitor.py and dashboard.py
- Removed unused variables (cid, situation_risks, date) to fix lint warnings

### Fixed
- High-priority lint issues (F405 star-import warnings, F841 unused variables)

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
