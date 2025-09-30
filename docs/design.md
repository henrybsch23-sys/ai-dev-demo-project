# Design Notes

Mini health-analytics demo used as a **playground** for an AI Developer Assistant
(Temporal-powered). Realistic structure:
- Core logic in `app/services/`
- REST endpoints in `app/api/`
- Tests in `tests/` (CI runs on PRs)

Typical AI tasks:
- Add a new calculator (e.g., VO2max estimate)
- Extend `/recommendations` with new rule
- Create CLI wrapper
- Improve input validation or typing
