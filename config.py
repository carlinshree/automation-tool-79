import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "log_level": "INFO",
    "max_retries": 3,
    "timeout": 30,
    "enabled": True
}

def load_config(config_path: str) -> Dict[str, Any]:
    """
    Loads configuration from a JSON file and merges with defaults.
    If file is missing, returns the default configuration dictionary.
    """
    config = DEFAULT_CONFIG.copy()

    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError):
            # Fallback to defaults on read/parse errors
            pass

    return config

def save_config(config_path: str, config: Dict[str, Any]) -> None:
    """
    Persists the current configuration dictionary to a JSON file.
    """
    try:
        with open(config_path, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        raise RuntimeError(f"Failed to save configuration: {e}")