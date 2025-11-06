"""
Test Project Generation
"""

import json
import shutil
import subprocess
from copy import deepcopy
from pathlib import Path
from typing import (
    Dict,
    Generator,
)

import pytest

THIS_DIR = Path(__file__).parent
PROJECT_DIR = THIS_DIR / "../"


@pytest.fixture(scope="function")
def project_dir() -> Generator[Path, None, None]:
    template_values = {
        "repo_name": "test_repo",
    }
    generated_proj_dir: Path = generate_project(template_value=template_values)
    yield generated_proj_dir
    shutil.rmtree(path=generated_proj_dir)


def generate_project(template_value: Dict[str, str]):
    """
    execute: cookiecutter <template directory> ...
    """
    # NOTE: dicionary is modified by cookiecutter, so we deepcopy it(arg is pointer)
    template_values: Dict[str, str] = deepcopy(template_value)

    cookiecutter_config = {"default_context": template_values}
    cookiecutter_config_fpath = PROJECT_DIR / "tests/cookiecutter_test_config.json"
    cookiecutter_config_fpath.write_text(json.dumps(cookiecutter_config))

    cmd = [
        "cookiecutter",
        str(PROJECT_DIR),
        "--output-dir",
        str(PROJECT_DIR / "sample"),
        "--no-input",
        "--config-file",
        str(cookiecutter_config_fpath),
        "--verbose",
    ]

    subprocess.run(cmd, check=True)
    generated_proj_dir = PROJECT_DIR / "sample" / template_values["repo_name"]
    return generated_proj_dir


def test_can_generate_project(project_dir: Path):
    """Test that project can be generated."""
    assert project_dir.exists()
