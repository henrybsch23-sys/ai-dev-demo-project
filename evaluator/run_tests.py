from __future__ import annotations
import subprocess
import json
from typing import TypedDict, Optional


class TestRunResult(TypedDict, total=False):
    returncode: int
    passed: bool
    stdout: str
    stderr: str
    junitxml: Optional[str]


def run_pytests(
    repo_root: str = ".",
    junitxml_path: str | None = None,
    quiet: bool = True,
    extra_args: list[str] | None = None,
) -> TestRunResult:
    """
    Run pytest in `repo_root`.

    Args:
        junitxml_path: if provided, writes a JUnit XML file at this path
        quiet: if True, runs with -q
        extra_args: extra pytest args (e.g. ["-k", "unit"])

    Returns:
        dict with returncode, passed, stdout, stderr, junitxml
    """
    cmd = ["pytest"]
    if quiet:
        cmd.append("-q")
    if junitxml_path:
        cmd.append(f"--junitxml={junitxml_path}")
    if extra_args:
        cmd.extend(extra_args)

    proc = subprocess.run(
        cmd, cwd=repo_root, capture_output=True, text=True
    )

    return {
        "returncode": proc.returncode,
        "passed": proc.returncode == 0,
        "stdout": proc.stdout[-8000:],  # trim to avoid huge payloads
        "stderr": proc.stderr[-8000:],
        "junitxml": junitxml_path,
    }
