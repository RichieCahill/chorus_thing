"""tests."""

from datetime import UTC, datetime

from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import AbstractConcreteBase
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import ForeignKey


class ChorusThing(DeclarativeBase):
    """A base class for contacts."""

    metadata = MetaData(schema="chorus_thing")


class BaseTable(AbstractConcreteBase, ChorusThing):
    """A base class for tables."""

    id: Mapped[int] = mapped_column(primary_key=True)
    created: Mapped[datetime] = mapped_column(default=datetime.now(tz=UTC))
    modified: Mapped[datetime] = mapped_column(default=datetime.now(tz=UTC), onupdate=datetime.now(tz=UTC))


class Event(BaseTable):
    """Table of Choral Events."""

    __tablename__ = "event"

    paid_event: Mapped[bool] = mapped_column(default=False)
    location: Mapped[str]
    event_time: Mapped[datetime] = mapped_column(default=datetime.now(tz=UTC), onupdate=datetime.now(tz=UTC))
    necessary_size: Mapped[int]

    def __repr__(self) -> str:
        """String representation of table."""
        return f"Event(event_time={self.event_time}, location={self.location}, paid_event={self.paid_event}, necessary_size={self.necessary_size})"
