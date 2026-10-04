import os
import json
import logging

# Configure application settings with fallback mechanisms
DEFAULT_CONFIG = {
    "max_retries": 3,
    "timeout": 30,
    "log_level": "INFO"
}

def load_config(filepath: str) -> dict:
    """Loads configuration from a JSON file with validation."""
    if not os.path.exists(filepath):
        logging.warning(f"Config file missing at {filepath}, using defaults")
        return DEFAULT_CONFIG

    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            if not isinstance(data, dict):
                raise ValueError("Invalid config format: expected dictionary")
            return {**DEFAULT_CONFIG, **data}
    except json.JSONDecodeError:
        logging.error(f"Malformed JSON in {filepath}")
        return DEFAULT_CONFIG
    except (PermissionError, OSError) as e:
        logging.error(f"File access error {filepath}: {e}")
        return DEFAULT_CONFIG

def validate_config(config: dict) -> bool:
    """Ensures critical keys exist in configuration."""
    required_keys = ['max_retries', 'timeout']
    try:
        return all(k in config for k in required_keys)
    except TypeError:
        return False