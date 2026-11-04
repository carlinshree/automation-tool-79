import json
import os
from typing import Any, Dict, Optional

DEFAULT_CONFIG: Dict[str, Any] = {
    "app_name": "automation-tool-79",
    "version": "1.0.0",
    "debug": False,
    "log_level": "INFO",
    "max_retries": 3,
    "timeout": 30,
    "output_dir": "./output",
}


class ConfigLoader:
    """Loads configuration settings from files with default fallbacks."""

    def __init__(self, config_path: Optional[str] = None):
        self.config_path = config_path
        self._config: Dict[str, Any] = DEFAULT_CONFIG.copy()
        if config_path:
            self.load()

    def load(self) -> Dict[str, Any]:
        """Loads configuration from a JSON file and merges with defaults."""
        if not self.config_path or not os.path.exists(self.config_path):
            return self._config

        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                user_config = json.load(f)
                if isinstance(user_config, dict):
                    self._config.update(user_config)
        except (json.JSONDecodeError, OSError) as err:
            print(f"Warning: Failed to load config from {self.config_path}: {err}")

        return self._config

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value by key."""
        return self._config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Set or update a configuration setting."""
        self._config[key] = value

    def save(self, target_path: Optional[str] = None) -> bool:
        """Save current configuration to a JSON file."""
        path = target_path or self.config_path
        if not path:
            return False

        try:
            os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                json.dump(self._config, f, indent=4)
            return True
        except OSError:
            return False
