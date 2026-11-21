from expense_tracker import storage
from expense_tracker.models import Expense


def test_save_and_load(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, "DATA_DIR", str(tmp_path))
    storage.add_expense(Expense(amount=1200, category="food", note="lunch", date="2026-03-01"))
    loaded = storage.load_expenses()
    assert len(loaded) == 1
    assert loaded[0].note == "lunch"


def test_load_missing_file(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, "DATA_DIR", str(tmp_path))
    assert storage.load_expenses() == []
