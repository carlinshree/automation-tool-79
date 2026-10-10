import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "retry_limit": 3,
    "timeout": 30,
    "log_level": "INFO",
    "enabled": True
}

def load_config(filepath: str) -> Dict[str, Any]:
    """
    Loads configuration from JSON file with fallback defaults.
    """
    config = DEFAULT_CONFIG.copy()

    if not os.path.exists(filepath):
        return config

    try:
        with open(filepath, 'r') as f:
            user_config = json.load(f)
            config.update(user_config)
    except (json.JSONDecodeError, IOError):
        pass

    return config

def save_config(filepath: str, data: Dict[str, Any]) -> None:
    """
    Persists configuration dictionary to JSON file.
    """
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)