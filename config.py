import json
import os
from typing import Any, Dict, Optional

DEFAULT_CONFIG: Dict[str, Any] = {
    "app_name": "automation-tool-79",
    "log_level": "INFO",
    "max_retries": 3,
    "timeout": 30,
    "enable_telemetry": False,
    "output_dir": "./output",
}


class ConfigLoader:
    """Handles loading configuration settings with fallback defaults."""

    def __init__(self, config_path: Optional[str] = None):
        self.config_path = config_path
        self._config: Dict[str, Any] = DEFAULT_CONFIG.copy()
        self._load_config()

    def _load_config(self) -> None:
        """Load settings from JSON file and environment variables."""
        if self.config_path and os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    file_config = json.load(f)
                    if isinstance(file_config, dict):
                        self._config.update(file_config)
            except (json.JSONDecodeError, OSError):
                pass

        # Override settings using environment variables if present
        for key in self._config:
            env_key = f"APP_{key.upper()}"
            if env_key in os.environ:
                self._config[key] = os.environ[env_key]

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value by key."""
        return self._config.get(key, default)

    def to_dict(self) -> Dict[str, Any]:
        """Return a copy of the active configuration dict."""
        return self._config.copy()
