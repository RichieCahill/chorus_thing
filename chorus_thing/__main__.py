"""Main module."""

from __future__ import annotations

from sqlalchemy import create_engine

from chorus_thing.app import create_app
from chorus_thing.database import Chorusitem

if __name__ == "__main__":
    engine = create_engine("sqlite://", echo=True)
    Chorusitem.metadata.create_all(engine)

    APP = create_app()
    APP.run(host="0.0.0.0", port=5000, debug=True)  # noqa: S104
