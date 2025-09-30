"""
Evaluator package

Small helpers to:
- apply a unified diff to the working directory
- run pytest and capture results
- compute a simple numeric score

All functions are pure-ish and return dictionaries so they’re easy to serialize.
"""
__all__ = ["apply_unified_diff", "run_pytests", "score_result"]
