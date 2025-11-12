"""
Helper functions for project generation tests.
"""

import json
import subprocess
from copy import deepcopy
from pathlib import Path
from typing import Dict

## Import project directory constant(funciona mesmo nao sendo full qualified page- video 159)
from tests.const import PROJECT_DIR


def initialize_git_repo(repo_dir: Path):
    """
    execute: git init and git commit, necessary for pre-commit hooks to work
    """
    subprocess.run(["git", "init"], cwd=repo_dir, check=True)
    subprocess.run(["git", "add", "--all"], cwd=repo_dir, check=True)
    subprocess.run(["git", "commit", "-m", "'feat: initial commit by pytest'"], cwd=repo_dir, check=True)
    subprocess.run(["git", "branch", "-m", "main"], cwd=repo_dir, check=True)


def generate_project(template_value: Dict[str, str], test_session_id: str):
    """
    execute: cookiecutter <template directory> ...
    """
    # NOTE: dicionary is modified by cookiecutter, so we deepcopy it(arg is pointer)
    template_values: Dict[str, str] = deepcopy(template_value)

    cookiecutter_config = {"default_context": template_values}
    cookiecutter_config_fpath = PROJECT_DIR / f"tests/cookiecutter_test_config_{test_session_id}.json"
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
    return generated_proj_dir
