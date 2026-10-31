from typing import Final, Dict, Any

# Configuration constants for automation-tool-79

TIMEOUT_SECONDS: Final[int] = 30
MAX_RETRIES: Final[int] = 3

DEFAULT_HEADERS: Final[Dict[str, str]] = {
    "User-Agent": "automation-tool-79/1.0.0",
    "Content-Type": "application/json",
}

LOG_LEVELS: Final[Dict[str, int]] = {
    "DEBUG": 10,
    "INFO": 20,
    "WARNING": 30,
    "ERROR": 40,
    "CRITICAL": 50,
}

def get_retry_delay(attempt: int) -> float:
    """Calculates exponential backoff delay based on attempt number."""
    return float(2 ** attempt)

class AppConfig:
    """Container for global application state constants."""
    def __init__(self, environment: str = "production") -> None:
        self.environment: str = environment
        self.base_url: str = "https://api.automation-tool-79.internal"

# Standardized path templates
PATH_STORAGE: Final[str] = "/var/lib/automation-tool-79/data"
PATH_LOGS: Final[str] = "/var/log/automation-tool-79"