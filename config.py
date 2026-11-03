import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "timeout": 30,
    "retries": 3,
    "log_level": "INFO",
    "enabled": True
}

def load_config(file_path: str = "config.json") -> Dict[str, Any]:
    """Load configuration from file, merging with default values."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not read config file {file_path}: {e}")
    
    return config

def get_setting(key: str, default_fallback: Any = None) -> Any:
    """Retrieve specific setting from the loaded environment."""
    config = load_config()
    return config.get(key, default_fallback)

if __name__ == "__main__":
    # Example usage for automation-tool-79
    current_config = load_config()
    print(f"Active configuration: {current_config}")