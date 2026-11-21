# Acceptance criteria

These must remain true after every change. Each one is checked by a test or a manual command.

| ID | Criterion | How it is checked |
|----|-----------|-------------------|
| AC1 | `add` saves an expense and `list` shows it with the same id, date, category and amount. | `tests/test_storage.py::test_save_and_load`, manual run |
| AC2 | `summary YYYY-MM` shows per-category sums and a TOTAL equal to the sum of that month's expenses only. | `tests/test_report.py` month tests, manual run |
| AC3 | Over-limit warnings appear for the same categories and limits as v0.3.0 (food 60000, transport 15000, entertainment 20000, utilities 35000, other 10000). | `tests/test_report.py` limit tests |
| AC4 | Existing `expenses.json` files written by v0.3.0 load without changes. | `test_save_and_load`, loading the baseline sample file |
| AC5 | `python -m pytest -q` passes and `ruff check .` reports no errors. | CI-style local run |
