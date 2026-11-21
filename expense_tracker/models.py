from dataclasses import dataclass, asdict
from datetime import date
import uuid


@dataclass
class Expense:
    amount: float
    category: str
    note: str
    date: str
    id: str = ""

    def __post_init__(self):
        if not self.id:
            self.id = uuid.uuid4().hex[:8]
        if not self.date:
            self.date = date.today().isoformat()

    def to_dict(self):
        return asdict(self)

    @staticmethod
    def from_dict(d):
        return Expense(
            amount=d["amount"],
            category=d["category"],
            note=d.get("note", ""),
            date=d["date"],
            id=d.get("id", ""),
        )
