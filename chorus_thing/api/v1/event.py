"""Provides Event data routes for the app."""

from flask import Blueprint, Sequence, request
from sqlalchemy import select
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from chorus_thing.database import Event

event_page = Blueprint("event_page", __name__)


@event_page.route("/event/", methods=("POST"))
def add_event(engine: Engine) -> str:
    """Add Event to Database."""
    paid_event = request.form.get("paid_event", False)
    location = request.form["location"]
    event_time = request.form.get("event_time", None)
    necessary_size = request.form["necessary_size"]
    choral_arrangement = request.form.get("choral_arrangement", "SATB")
    event = Event(
        paid_event=paid_event,
        location=location,
        event_time=event_time,
        necessary_size=necessary_size,
        choral_arrangement=choral_arrangement,
    )
    with Session(engine) as session:
        event = Event(
            paid_event=paid_event,
            location=location,
            event_time=event_time,
            necessary_size=necessary_size,
            choral_arrangement=choral_arrangement,
        )
        session.add(event)
        session.commit()
    return str(event)


@event_page.route("/event/<location>", methods=("GET"))
def get_event(location: str, engine: Engine) -> Sequence[Event]:
    """Find Event in Database."""
    statement = select(Event).where(location=location)
    with Session(engine) as session:
        return session.scalars(statement).all()


@event_page.route("/event/<location>", methods=("PUT"))
def update_event(location: str, engine: Engine) -> Sequence[Event]:
    """Update Event in Database."""
    statement = select(Event).where(Event.location=location)
    with Session(engine) as session:
        event_list = session.scalars(statement).all()
        for event in event_list:
            for k, v in request.form:
                event[k] = v
            session.commit()
    return event_list


@event_page.route("/event/<location>", methods=("DELETE"))
def delete_event(location: str, engine: Engine) -> Sequence[Event]:
    """Delete Event in Database."""
    statement = select(Event).where(Event.location=location)
    with Session(engine) as session:
        event_list = session.scalars(statement).all()
        for event in event_list:
            session.delete(event)
            session.commit()
    return event_list
