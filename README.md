# Expense Tracker

Small command line tool to track my monthly expenses in tenge (KZT).
Data is kept in a JSON file in `~/.expenses/`.

## Install

```
pip install -r requirements.txt
```

## Usage

```
python main.py add 2500 food --note "lunch"
python main.py list
python main.py summary 2026-03
python main.py export march.csv
```

Categories: food, transport, entertainment, utilities. Anything else goes to "Other".
Each category has a monthly limit, the summary prints a warning when you go over it.

## Tests

```
pytest
```
