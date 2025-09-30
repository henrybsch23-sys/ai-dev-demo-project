from __future__ import annotations
import pathlib
import subprocess
import tempfile
from typing import Literal, TypedDict


class ApplyPatchResult(TypedDict):
    ok: bool
    applied: bool
    message: str


def apply_unified_diff(
    patch_text: str,
    repo_root: str | pathlib.Path = ".",
    check_conflicts: bool = True,
) -> ApplyPatchResult:
    """
    Apply a unified diff to the git working tree.

    - Writes `patch_text` to a temp file.
    - If `check_conflicts` is True, we first run `git apply --check` to validate.
    - Then we run `git apply` to modify the working tree.

    Returns:
        { ok, applied, message }
    """
    repo_root = pathlib.Path(repo_root)
    patch_file = pathlib.Path(tempfile.mkstemp(suffix=".patch")[1])
    patch_file.write_text(patch_text, encoding="utf-8")

    try:
        if check_conflicts:
            check = subprocess.run(
                ["git", "apply", "--check", str(patch_file)],
                cwd=repo_root,
                capture_output=True,
                text=True,
            )
            if check.returncode != 0:
                return {
                    "ok": False,
                    "applied": False,
                    "message": f"Patch check failed:\n{check.stderr or check.stdout}",
                }

        proc = subprocess.run(
            ["git", "apply", str(patch_file)],
            cwd=repo_root,
            capture_output=True,
            text=True,
        )
        if proc.returncode != 0:
            return {
                "ok": False,
                "applied": False,
                "message": f"Patch apply failed:\n{proc.stderr or proc.stdout}",
            }

        return {"ok": True, "applied": True, "message": "Patch applied"}
    finally:
        try:
            patch_file.unlink(missing_ok=True)
        except Exception:
            pass
