import os
import re
from urllib.parse import urlparse

# Regular expression for basic email validation
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")


def is_valid_url(url: str) -> bool:
    """Check if a string is a valid HTTP or HTTPS URL."""
    if not url:
        return False
    try:
        parsed = urlparse(url)
        return parsed.scheme in ("http", "https") and bool(parsed.netloc)
    except ValueError:
        return False


def is_valid_email(email: str) -> bool:
    """Check if a string matches a basic email pattern."""
    if not email:
        return False
    return bool(EMAIL_REGEX.match(email))


def find_missing_paths(paths: list) -> list:
    """Verify existence of required file paths and return a list of missing ones."""
    missing = []
    for path in paths:
        if not isinstance(path, str):
            missing.append(str(path))
        elif not os.path.exists(path):
            missing.append(path)
    return missing


def validate_cron_expression(cron: str) -> bool:
    """Validate standard 5-field cron expressions in a simplistic manner."""
    if not cron or not isinstance(cron, str):
        return False
    parts = cron.split()
    return len(parts) == 5
