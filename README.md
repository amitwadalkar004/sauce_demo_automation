# Sauce Demo UI Automation Framework

A Python + Playwright UI automation framework scaffold for the Sauce Demo web application.

## Features

- Page Object Model (POM)
- Pytest-based test execution
- Playwright browser automation
- Configurable base URL and credentials
- GitHub Actions workflow for CI

## Setup

1. Create a virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   playwright install
   ```

## Run tests

```powershell
pytest
```

## Project structure

- `pages/` - Page objects for the Sauce Demo app
- `tests/` - Test cases and fixtures
- `utils/` - Configuration and shared helpers
- `.github/workflows/` - CI workflow for GitHub Actions
