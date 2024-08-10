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


class Event(BaseTable):
    """Table of Choral Events."""

    __tablename__ = "event"

    paid_event: Mapped[bool] = mapped_column(default=False)
    location: Mapped[str]
    event_time: Mapped[datetime | None]
    necessary_size: Mapped[int]
    choral_arrangement: Mapped[str] = mapped_column(default="SATB")

    def __repr__(self) -> str:
        """String representation of table."""
        return f"""Event(event_time={self.event_time}, location={self.location}, paid_event={self.paid_event},
        choral_arrangement={self.choral_arrangement}, necessary_size={self.necessary_size})"""


class MusicLibrary(BaseTable):
    """A class for scores."""

    __tablename__ = "music_library"

    title: Mapped[str]
    composer: Mapped[str]
    lyricist: Mapped[str | None]
    instrumentation: Mapped[str]
    language: Mapped[str]
    publisher: Mapped[str | None]
    publication_number: Mapped[str | None]
    score_link: Mapped[str | None]
    lyric_link: Mapped[str | None]
    track01_link: Mapped[str | None]
    track02_link: Mapped[str | None]
    track03_link: Mapped[str | None]
    track04_link: Mapped[str | None]
    track05_link: Mapped[str | None]
    track06_link: Mapped[str | None]
    track07_link: Mapped[str | None]
    track08_link: Mapped[str | None]
    track09_link: Mapped[str | None]
    num_copies: Mapped[str]
    license_info: Mapped[str | None]
