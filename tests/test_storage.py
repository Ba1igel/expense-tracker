import pytest

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


# R-02 regression tests: export must stay inside the data directory


@pytest.mark.parametrize("bad_name", ["../outside.csv", "../../etc/x.csv", "/tmp/abs.csv", "sub/dir.csv", ""])
def test_export_rejects_paths_outside_data_dir(tmp_path, monkeypatch, bad_name):
    data = tmp_path / "data"
    monkeypatch.setattr(storage, "DATA_DIR", str(data))
    with pytest.raises(ValueError):
        storage.export_csv([], bad_name)
    assert not (tmp_path / "outside.csv").exists()


def test_export_plain_filename_works(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, "DATA_DIR", str(tmp_path))
    out = storage.export_csv([Expense(amount=1000, category="food", note="", date="2026-03-01")], "march.csv")
    assert out == str(tmp_path / "march.csv")
    assert (tmp_path / "march.csv").read_text().startswith("id,date,category,amount,note")
