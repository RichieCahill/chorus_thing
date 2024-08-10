"""tests."""

from datetime import UTC, datetime

from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import AbstractConcreteBase
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class ChorusThing(DeclarativeBase):
    """A base class for contacts."""

    metadata = MetaData(schema="chorus_thing")


class BaseTable(AbstractConcreteBase, ChorusThing):
    """A base class for tables."""

    id: Mapped[int] = mapped_column(primary_key=True)
    created: Mapped[datetime] = mapped_column(default=datetime.now(tz=UTC))
    modified: Mapped[datetime] = mapped_column(default=datetime.now(tz=UTC), onupdate=datetime.now(tz=UTC))
