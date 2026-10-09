from typing import Any, Dict, Optional

def validate_payload(data: Any, schema: Dict[str, type]) -> bool:
    """
    Checks if input data matches the provided dictionary schema.
    Returns True if valid, False otherwise.
    """
    if not isinstance(data, dict):
        return False

    for key, expected_type in schema.items():
        if key not in data:
            return False
        if not isinstance(data[key], expected_type):
            return False
            
    return True

def sanitize_input(value: Any) -> Any:
    """
    Trims strings and ensures basic data integrity.
    """
    if isinstance(value, str):
        return value.strip()
    if value is None:
        return ""
    return value

def format_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Applies sanitization to all fields in a dictionary.
    """
    return {k: sanitize_input(v) for k, v in data.items()}