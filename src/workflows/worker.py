"""
Non-Temporal stub.

If you later want a local simulation of "background tasks" (e.g., pre-commit checks,
code formatters), you can place simple functions here and call them from scripts.
"""
from __future__ import annotations


def simulate_code_check(content: str) -> bool:
    """Pretend to check code quality; returns True if 'TODO' not present."""
    return "TODO" not in content
