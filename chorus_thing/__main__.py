"""Main module."""

from __future__ import annotations

import logging

from chorus_thing.common import configure_logger


def main() -> None:
    """Main function."""
    configure_logger()

    logging.info("Hello World")


if __name__ == "__main__":
    main()
