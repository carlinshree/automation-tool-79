import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "log_level": "INFO",
    "max_retries": 3,
    "timeout": 30
}

def load_config(file_path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from a JSON file with defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not read config file {file_path}: {e}")
            
    return config

def get_config_value(key: str, config: Dict[str, Any]) -> Any:
    """Retrieves a value from the loaded config dictionary."""
    return config.get(key, DEFAULT_CONFIG.get(key))