import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "log_level": "INFO",
    "max_retries": 3,
    "timeout": 30,
    "enabled": True
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """
    Loads configuration from a JSON file with fallbacks.
    If the file is missing, returns the default settings.
    """
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading config file: {e}. Using defaults.")
            
    return config

if __name__ == "__main__":
    # Example usage demonstration
    current_config = load_config()
    print(f"Configuration loaded: {current_config}")