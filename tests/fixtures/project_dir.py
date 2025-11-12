"""
Fixture to generate a project directory for testing.
"""

import shutil
import subprocess
from pathlib import Path
from typing import Generator
from uuid import uuid4

import pytest

from tests.utils.project import (
    generate_project,
    initialize_git_repo,
)


@pytest.fixture(scope="session")
def project_dir() -> Generator[Path, None, None]:
    test_session_id: str = generate_test_session_id()
    template_values = {
        "repo_name": f"test_repo_{test_session_id}",
    }
    generated_proj_dir: Path = generate_project(template_value=template_values, test_session_id=test_session_id)
    try:
        initialize_git_repo(generated_proj_dir)
        # Run linting to fix any formatting issues in the generated project antes dos testes com o mesmo commando
        subprocess.run(["make", "lint-ci"], cwd=generated_proj_dir, check=False)
        yield generated_proj_dir
    finally:
        shutil.rmtree(path=generated_proj_dir)


def generate_test_session_id() -> str:
    return str(uuid4())[:6]
