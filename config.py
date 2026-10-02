import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "timeout": 30,
    "retries": 3,
    "log_level": "INFO",
    "enabled": True
}

def load_config(config_path: str) -> Dict[str, Any]:
    """
    Loads configuration from a JSON file with system defaults.
    Returns the merged configuration dictionary.
    """
    config = DEFAULT_CONFIG.copy()

    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load config {config_path}: {e}")
            
    return config

def get_setting(key: str, config_path: str = "config.json") -> Any:
    """
    Retrieves a single setting value from the config loader.
    """
    return load_config(config_path).get(key, DEFAULT_CONFIG.get(key))

if __name__ == "__main__":
    # Demonstration of default usage
    current_config = load_config("settings.json")
    print(f"Loaded configuration: {current_config}")