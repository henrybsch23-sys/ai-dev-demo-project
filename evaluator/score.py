from __future__ import annotations
from typing import TypedDict


class ScoreInput(TypedDict, total=False):
    passed: bool
    returncode: int
    stdout: str
    stderr: str


def score_result(test_result: ScoreInput) -> float:
    """
    Simple, explainable scoring:
    - Base: 1.0 if tests pass, else 0.0
    - (Optional extensions: lint bonuses/deductions, touched file rules, etc.)

    Keep it boring and reliable for the hackathon demo.
    """
    return 1.0 if bool(test_result.get("passed")) else 0.0
