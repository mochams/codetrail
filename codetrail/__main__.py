"""Entrypoint to our cli application."""

from codetrail.logconfig import logger


def main() -> None:
    """Entrypoint for the version control system."""
    logger.info("You've reached entrypoint, Hello Codetrail!")


if __name__ == "__main__":
    main()
