from expense_tracker.categories import DEFAULT_RULE, RULES, rule_for


def test_unknown_category_uses_default_rule():
    assert rule_for("gifts") is DEFAULT_RULE


def test_known_categories():
    assert set(RULES) == {"food", "transport", "entertainment", "utilities"}


def test_is_over_limit_is_strict():
    assert not RULES["food"].is_over_limit(60000)
    assert RULES["food"].is_over_limit(60001)
