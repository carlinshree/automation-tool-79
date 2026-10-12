import re
from typing import Any, Optional

def validate_email(email: str) -> bool:
    """Checks if the provided string follows a standard email format."""
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(email_pattern, email))

def sanitize_input(data: Any) -> Optional[str]:
    """Removes potential script tags and whitespace for string inputs."""
    if not isinstance(data, str):
        return None
    
    cleaned = re.sub(r'<[^>]*?>', '', data)
    return cleaned.strip()

def check_type_consistency(data: Any, expected_type: type) -> bool:
    """Verifies that the provided data matches the expected type."""
    return isinstance(data, expected_type)

def validate_numeric_range(value: float, min_val: float, max_val: float) -> bool:
    """Ensures a number falls within inclusive bounds."""
    try:
        return min_val <= float(value) <= max_val
    except (ValueError, TypeError):
        return False