import re
from typing import Any, Optional

# regex patterns for validation
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

def validate_email(email: str) -> bool:
    """verify email format correctness"""
    return bool(EMAIL_REGEX.match(email))

def validate_non_empty(value: Any) -> bool:
    """check if provided input is not empty"""
    if value is None:
        return False
    if isinstance(value, str):
        return len(value.strip()) > 0
    return bool(value)

def sanitize_input(value: str) -> str:
    """strip whitespace and clean string input"""
    return str(value).strip()

class ValidationError(Exception):
    """custom exception for validation failures"""
    pass

def assert_valid_email(email: Optional[str]) -> str:
    """raise exception if email is invalid"""
    if not email or not validate_email(email):
        raise ValidationError(f"Invalid email format: {email}")
    return email