"""Category rules: one place for the label and monthly limit of every category.

Adding a category = adding one line to RULES. Nothing else has to change.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class CategoryRule:
    label: str
    monthly_limit: int  # KZT

    def is_over_limit(self, spent: float) -> bool:
        return spent > self.monthly_limit


RULES: dict[str, CategoryRule] = {
    "food": CategoryRule("Food & groceries", 60000),
    "transport": CategoryRule("Transport", 15000),
    "entertainment": CategoryRule("Entertainment", 20000),
    "utilities": CategoryRule("Utilities", 35000),
}

DEFAULT_RULE = CategoryRule("Other", 10000)


def rule_for(category: str) -> CategoryRule:
    return RULES.get(category, DEFAULT_RULE)
