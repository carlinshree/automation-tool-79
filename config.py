import json
import os
from typing import Any, Dict, Optional

DEFAULT_CONFIG: Dict[str, Any] = {
    "app_name": "AutomationTool",
    "version": "1.0.0",
    "log_level": "INFO",
    "max_retries": 3,
    "timeout": 30,
    "output_dir": "./output",
    "enable_notifications": False,
}


class ConfigLoader:
    """Loads and merges configuration settings with default fallback values."""

    def __init__(self, config_path: Optional[str] = None):
        self.config_path = config_path
        self._config: Dict[str, Any] = DEFAULT_CONFIG.copy()
        if config_path:
            self.load()

    def load(self, path: Optional[str] = None) -> Dict[str, Any]:
        """Load JSON configuration file and update defaults."""
        target_path = path or self.config_path
        if not target_path or not os.path.exists(target_path):
            return self._config

        try:
            with open(target_path, "r", encoding="utf-8") as f:
                user_config = json.load(f)
                if isinstance(user_config, dict):
                    self._config.update(user_config)
        except (json.JSONDecodeError, OSError) as err:
            print(f"Warning: Failed to load config from {target_path}: {err}")

        return self._config

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration option by key."""
        return self._config.get(key, default)

    @property
    def config(self) -> Dict[str, Any]:
        """Return the current configuration dictionary."""
        return self._config.copy()
