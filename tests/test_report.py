from expense_tracker.models import Expense
from expense_tracker import report


def make(amount, cat, d):
    return Expense(amount=amount, category=cat, note="", date=d)


def test_total():
    items = [make(1000, "food", "2026-03-01"), make(2500, "transport", "2026-03-02")]
    assert report.total(items) == 3500


def test_by_category():
    items = [make(1000, "food", "2026-03-01"), make(500, "food", "2026-03-05"), make(200, "transport", "2026-03-02")]
    assert report.by_category(items) == {"food": 1500, "transport": 200}


def test_filter_by_month():
    items = [make(1000, "food", "2026-03-01"), make(500, "food", "2026-04-05")]
    # NOTE: month is passed the same way the CLI does it
    result = report.filter_by_month(items, 2026, "03")
    assert len(result) == 1


def test_limit_warning_food():
    items = [make(70000, "food", "2026-03-01")]
    w = report.limit_warnings(items)
    assert len(w) == 1
    assert "Food" in w[0]


def test_no_warning_under_limit():
    items = [make(5000, "transport", "2026-03-01")]
    assert report.limit_warnings(items) == []
