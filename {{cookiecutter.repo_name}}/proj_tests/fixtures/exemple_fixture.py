"""Fixture to generate a project directory for testing."""

from uuid import uuid4

import pytest
from proj_tests.consts import PROJECT_DIR


@pytest.fixture(scope="session")
def generate_test_session_id() -> str:
    """Generate a unique test session ID."""
    return str(PROJECT_DIR.name) + str(uuid4())[:6]
