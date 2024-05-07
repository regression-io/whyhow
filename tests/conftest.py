"""Configuration for the tests."""

import pathlib

import pytest


@pytest.fixture
def test_path():
    """Return the path to the tests directory."""
    return pathlib.Path(__file__).parent


@pytest.fixture(autouse=True)
def delete_env_vars(monkeypatch):
    """Delete environment variables.

    This fixture is used to delete the environment variables that are used

    """
    monkeypatch.setenv("WHYHOW_API_KEY", "FAKE")
