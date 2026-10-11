from typing import Any, Dict, Optional

def validate_config(config: Dict[str, Any]) -> bool:
    """
    Validates that the provided configuration dictionary contains mandatory keys.

    :param config: Dictionary containing tool configuration settings
    :return: True if valid, False otherwise
    """
    required_keys = ['api_key', 'endpoint', 'timeout']
    return all(key in config for key in required_keys)

def sanitize_input(value: Any) -> str:
    """
    Converts input values to a cleaned string format.

    :param value: The input data to sanitize
    :return: Cleaned string representation
    """
    if value is None:
        return ""
    return str(value).strip()

def check_connection_status(status_code: Optional[int]) -> bool:
    """
    Verifies if a status code indicates a successful operation.

    :param status_code: The HTTP status code received
    :return: True if code is 200, False otherwise
    """
    if status_code is None:
        return False
    return status_code == 200