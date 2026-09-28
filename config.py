import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "timeout": 30,
    "retries": 3,
    "log_level": "INFO"
}

def load_config(filepath: str) -> Dict[str, Any]:
    """Loads configuration from a JSON file with defaults."""
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

def save_config(filepath: str, config: Dict[str, Any]) -> None:
    """Saves configuration dictionary to a JSON file."""
    with open(filepath, 'w') as f:
        json.dump(config, f, indent=4)