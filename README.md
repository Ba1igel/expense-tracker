# Expense Tracker

Small command line tool to track my monthly expenses in tenge (KZT).
Data is kept in a JSON file in `~/.expenses/` (can be changed with the `EXPENSES_DIR` environment variable).

## Install

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
```

## Usage

```
python -m expense_tracker add 2500 food --note "lunch"
python -m expense_tracker list
python -m expense_tracker summary 2026-03
python -m expense_tracker export march.csv
```

Categories: food, transport, entertainment, utilities. Anything else goes to "Other".
Each category has a monthly limit, the summary prints a warning when you go over it.

## Tests

```
python -m pytest -q
ruff check .
mypy expense_tracker
```

Notes for AI agents and contributors are in `AGENTS.md`, acceptance criteria in `docs/acceptance-criteria.md`.
