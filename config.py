import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "log_level": "INFO",
    "max_retries": 3,
    "timeout": 30
}

def load_config(file_path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from json file with defaults fallback."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError):
            pass
            
    return config

def save_config(config: Dict[str, Any], file_path: str = "config.json") -> None:
    """Persists current configuration state to disk."""
    with open(file_path, 'w') as f:
        json.dump(config, f, indent=4)