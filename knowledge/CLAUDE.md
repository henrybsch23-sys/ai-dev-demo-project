# Team Conventions (CLAUDE.md)

This file gives the AI developer the “house rules.” Keep changes small and explicit so tests stay deterministic.

## Code Style
- Python 3.11
- FastAPI for HTTP, pytest for tests
- Prefer pure functions in `src/services/*` and thin FastAPI routes in `src/api/main.py`
- Raise `ValueError` for invalid inputs in service layer; map to HTTP 400 in API layer

## Testing
- Add/modify tests under `src/tests/*`
- Keep assertions specific and stable (avoid brittle string matching)
- Aim for green tests locally with `pytest -q`

## Safety / Scope
- Do not touch secrets, CI config, or dependency pins unless acceptance criteria explicitly require it.
- Keep diffs minimal and focused on acceptance criteria.

## Endpoints (current)
- `GET /health`
- `GET /bmi?weight_kg&height_m`
- `GET /bmr?sex&weight_kg&height_cm&age`
- `GET /tdee?bmr_val&activity` (valid: `sedentary`, `light`, `moderate`, `active`, `very_active`)
- `GET /bodyfat?sex&height_cm&neck_cm&waist_cm&hip_cm?`
- `GET /water?weight_kg&activity_hours`
- `GET /recommendations?weight_kg&height_m&activity_hours`

## Patch Format
- Submit patches as unified diffs against repo root.
- Keep within `src/` and `src/tests/` unless otherwise stated.

## Review Checklist
- ✅ Acceptance criteria satisfied
- ✅ Tests added/updated and passing
- ✅ API error handling returns 400 on invalid inputs
- ✅ Minimal, readable diffs
