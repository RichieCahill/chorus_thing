"""App."""

from __future__ import annotations

from flask import Flask, Response, json

from chorus_thing.common import configure_logger

from chorus_thing.database import MusicLibrary


def create_app() -> Flask:
    """Create the Flask app."""
    app = Flask(__name__)
    configure_logger()

    @app.route("/")
    def hello_world() -> str:
        """Hello world."""
        return "Hello World"

    return app


def get_endpoint() -> Flask:
    """Create a get endpoint."""
    app = Flask(__name__)

    @app.get("/request")
    def request_get() -> str:
        """Pee pee."""
        return "Pee pee"

    @app.post("/request")
    def request_post() -> str:
        """Poo poo."""
        return "Poo poo"


def endpoints() -> Flask:
    """Create a get/post endpoint."""
    app = Flask(__name__)

    @app.route("/requests", methods=["GET," "POST"])
    def requests(request: Response) -> str:
        """Pee pee poo poo."""
        if request.method == "GET":
            return "Pee pee"
        if request.method == "POST":
            return "Poo poo"
        raise RuntimeError


def get_json() -> Flask:
    """Accept and read json content."""
    app = Flask(__name__)

    @app.route("/json", methods=["POST"])
    def accept_json(request: Response) -> None:
        data = request.json
        print(data)
        MusicLibrary(
            title = data["title"],
            composer = data["composer"],
            lyricist = data.get["lyricist"],
            instrumentation = data["instrumentation"],
            language = data["language"],
            publisher = data.get["publisher"],
            publication_number = data.get["publication_number"],
            score_link = data.get["score_link"],
            lyrics_link = data.get["lyrics_link"],
            number_copies = data["number_copies"],
            track01_link = data.get["track01_link"],
            track02_link = data.get["track02_link"],
            track03_link = data.get["track03_link"],
            track04_link = data.get["track04_link"],
            track05_link = data.get["track05_link"],
            track06_link = data.get["track06_link"],
            track07_link = data.get["track07_link"],
            track08_link = data.get["track08_link"],
            track09_link = data.get["track09_link"],
            license_info = data.get["license_info"]
            )
