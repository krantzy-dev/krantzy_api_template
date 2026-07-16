from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Shared declarative base for all ORM models. Import your models in
    src/models/__init__.py so Alembic autogenerate can discover them.
    """
