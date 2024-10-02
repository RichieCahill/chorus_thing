"""App."""

from __future__ import annotations

from flask import Flask

from chorus_thing.api.v1.event import event_page
from chorus_thing.common import configure_logger


def create_app() -> Flask:
    """Create the Flask app."""
    app = Flask(__name__)
    app.register_blueprint(event_page, url_prefix="/api/v1")
    configure_logger()

    @app.route("/")
    def hello_world() -> str:
        """Hello world."""
        return "Hello World"

    return app
