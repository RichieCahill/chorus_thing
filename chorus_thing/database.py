"""tests."""

import logging
from datetime import UTC, datetime
from typing import Self, cast

from sqlalchemy import MetaData, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import AbstractConcreteBase
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, object_session


def safe_object_session(class_: object) -> Session:
    """Get a session for a class."""
    if session := object_session(class_):
        return session
    error = f"No session found for {class_}"
    raise RuntimeError(error)


class Chorusitem(DeclarativeBase):
    """A base class for contacts."""

    metadata = MetaData(schema="chorus_item")


class BaseColumns:
    """Base columns."""

    id: Mapped[int] = mapped_column(primary_key=True)
    created: Mapped[datetime] = mapped_column(default=datetime.now(tz=UTC))
    modified: Mapped[datetime] = mapped_column(default=datetime.now(tz=UTC), onupdate=datetime.now(tz=UTC))


class BaseTable(BaseColumns, AbstractConcreteBase, Chorusitem):
    """A base class for tables."""


class BaseLookupTable(BaseColumns, AbstractConcreteBase, Chorusitem):
    """A lookup table."""

    name: Mapped[str] = mapped_column(primary_key=True)

    @classmethod
    def get(class_, name: str) -> Self | None:
        """Get a lookup table by name.

        Args:
            name (str): The name of the lookup table.

        Returns:
            BaseLookupTable | None: The lookup table, or None if not found.
        """
        return cast(Session, object_session(class_)).scalars(select(class_).where(class_.name == name)).one_or_none()

    @classmethod
    def add(class_, name: str) -> Self:
        """Add a lookup table.

        Args:
            name (str): The name of the lookup table.

        Returns:
            BaseLookupTable: The lookup table.
        """
        if item := class_.get(name):
            return item
        session = safe_object_session(class_)
        try:
            item = class_(name=name)
            session.add(item)
            session.commit()
        except IntegrityError:
            if item := class_.get(name):
                msg = f"Duplicate item in lookup table {name}"
                logging.info(msg)
                return item
            raise
        return item


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
    number_copies: Mapped[str]
    license_info: Mapped[str | None]


class Member(BaseTable):
    """Members."""

    __tablename__ = "Member Info"

    first_name: Mapped[str]
    middle_name: Mapped[str | None]
    last_name: Mapped[str]
    section: Mapped[str | None]
    member_since: Mapped[str | None]
    phone_number: Mapped[str | None]
    email: Mapped[str | None]
    address: Mapped[str | None]
    emergency_contact: Mapped[str | None]
    emergency_contact_phone_number: Mapped[str | None]

    def __repr__(self) -> str:
        """String representation of table."""
        return f"""Member(first_name={self.first_name}, last_name={self.last_name}, section={self.section},
        member_since={self.member_since}, phone_number={self.section}, email={self.email})"""
