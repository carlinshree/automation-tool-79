import re
from typing import Any, Optional

def is_valid_email(email: str) -> bool:
    """Verify email address format using regex."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))

def is_non_empty_string(value: Any) -> bool:
    """Check if input is a string and not blank."""
    return isinstance(value, str) and len(value.strip()) > 0

def validate_range(value: int, min_val: int, max_val: int) -> bool:
    """Check if integer resides within inclusive bounds."""
    return min_val <= value <= max_val

def sanitize_input(value: Optional[str]) -> str:
    """Remove whitespace and return empty string if None."""
    if not value:
        return ""
    return str(value).strip()

def validate_structure(data: dict, required_keys: list) -> bool:
    """Ensure dictionary contains all necessary keys."""
    return all(key in data for key in required_keys)