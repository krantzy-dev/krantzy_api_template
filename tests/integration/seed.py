import json
from pathlib import Path
from typing import Any

from sqlalchemy.orm import Session

FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"


def _load_fixture(name: str) -> Any:
    with (FIXTURES_DIR / name).open(encoding="utf-8") as f:
        return json.load(f)


def load_seed_data(db: Session) -> None:
    """Populate the test database with the shared fixture dataset.

    Add one `db.add_all(...)` block per model as the schema grows, mapping
    dicts from fixtures/seed_data.json onto the corresponding SQLAlchemy model.
    """
    _load_fixture("seed_data.json")
    db.commit()
