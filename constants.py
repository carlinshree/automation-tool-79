import logging
from typing import Final

# Application configuration and error thresholds
MAX_RETRIES: Final[int] = 3
TIMEOUT_SECONDS: Final[float] = 30.0
CHUNK_SIZE: Final[int] = 1024 * 1024

# Error handling constants
RETRYABLE_STATUS_CODES: Final[set[int]] = {408, 429, 500, 502, 503, 504}
DEFAULT_LOG_LEVEL: Final[int] = logging.INFO

# Path and format constraints
MAX_FILENAME_LENGTH: Final[int] = 255
SUPPORTED_EXTENSIONS: Final[tuple[str, ...]] = ('.json', '.csv', '.yaml')

def validate_environment() -> None:
    """verify required system constants are set correctly"""
    if MAX_RETRIES < 0:
        raise ValueError("retry count cannot be negative")
    if TIMEOUT_SECONDS <= 0:
        raise ValueError("timeout must be a positive number")

# Ensure environment integrity on import
validate_environment()