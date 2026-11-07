import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "log_level": "INFO",
    "max_retries": 3,
    "timeout": 30.0,
    "data_path": "./data"
}

def load_config(file_path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from json file or returns defaults."""
    config = DEFAULT_CONFIG.copy()

    if not os.path.exists(file_path):
        return config

    try:
        with open(file_path, "r") as f:
            user_config = json.load(f)
            config.update(user_config)
    except (json.JSONDecodeError, IOError):
        pass

    return config

def get_setting(key: str, default: Any = None) -> Any:
    """Helper to retrieve a specific setting value."""
    config = load_config()
    return config.get(key, default)