"""Main module."""

from __future__ import annotations

from chorus_thing.app import create_app

if __name__ == "__main__":
    APP = create_app()
    APP.run(host="0.0.0.0", port=5000, debug=True)  # noqa: S104
