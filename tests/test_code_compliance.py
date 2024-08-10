"""Test code compliance."""

from re import match
from subprocess import run


def run_command(command: str) -> tuple[bytes, int]:
    """Run a command.

    Args:
        command (str): Command to run.
    """
    process = run(command.split(), check=False, capture_output=True)  # noqa: S603 false positive
    return process.stdout, process.returncode


def test_ruff_check() -> None:
    """Test ruff check."""
    stdout, returncode = run_command("poetry run ruff check .")
    assert stdout.decode() == "All checks passed!\n"
    assert returncode == 0


def test_ruff_format() -> None:
    """Test ruff format."""
    stdout, returncode = run_command("poetry run ruff format --check .")
    assert match(r"\d files already formatted", stdout.decode())
    assert returncode == 0


def test_mypy_check() -> None:
    """Test mypy check."""
    stdout, returncode = run_command("poetry run mypy .")
    assert match(r"Success: no issues found in \d source files", stdout.decode())
    assert returncode == 0
