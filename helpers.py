import logging

logger = logging.getLogger(__name__)

def validate_input_data(data, required_keys):
    """
    Ensure input is a dictionary and contains all mandatory fields.
    Returns a tuple of (is_valid, error_message).
    """
    if not isinstance(data, dict):
        return False, "Input must be a dictionary object."
    
    missing_keys = [key for key in required_keys if key not in data]
    if missing_keys:
        return False, f"Missing mandatory keys: {', '.join(missing_keys)}"
    
    for key, value in data.items():
        if value is None:
            return False, f"Value for key '{key}' cannot be null."
            
    return True, None

def sanitize_input_string(value):
    """
    Basic stripping and normalization for string inputs.
    """
    if not isinstance(value, str):
        return str(value).strip()
    return value.strip()

def process_with_validation(data, schema):
    """
    Main loop entry point validation logic.
    """
    is_valid, error = validate_input_data(data, schema)
    if not is_valid:
        logger.error(f"Validation failure: {error}")
        raise ValueError(error)
    
    # Proceed with sanitized values
    return {k: sanitize_input_string(v) for k, v in data.items()}