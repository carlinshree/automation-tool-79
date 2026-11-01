import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Handles loading configuration from JSON files with fallback defaults."""

    DEFAULT_CONFIG = {
        "log_level": "INFO",
        "retries": 3,
        "timeout": 30
    }

    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """Loads configuration from file or returns defaults."""
        if not os.path.exists(self.config_path):
            return self.DEFAULT_CONFIG.copy()

        try:
            with open(self.config_path, "r") as f:
                user_config = json.load(f)
                return {**self.DEFAULT_CONFIG, **user_config}
        except (json.JSONDecodeError, IOError):
            return self.DEFAULT_CONFIG.copy()

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves a value from the configuration."""
        return self.config.get(key, default)

if __name__ == "__main__":
    loader = ConfigLoader()
    print(f"Loaded log level: {loader.get('log_level')}")