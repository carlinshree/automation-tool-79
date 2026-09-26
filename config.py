import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "retries": 3,
    "timeout": 30,
    "log_level": "INFO",
    "enabled": True
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """Load configuration from JSON file with fallback defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if not os.path.exists(filepath):
        return config
        
    try:
        with open(filepath, "r") as f:
            user_config = json.load(f)
            config.update(user_config)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Warning: failed to load config file: {e}")
        
    return config

def validate_config(config: Dict[str, Any]) -> bool:
    """Ensure required configuration keys are present."""
    required_keys = ["retries", "timeout"]
    return all(key in config for key in required_keys)