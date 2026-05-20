import pytest

from pathlib import Path

# Playwright configuration for local execution and CI
project_dir = Path(__file__).resolve().parent

pytest_plugins = ["pytest_playwright"]
