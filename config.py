import json
import os
from pathlib import Path
from typing import Any, Dict, Optional

DEFAULT_CONFIG: Dict[str, Any] = {
    "app_name": "automation-tool-79",
    "version": "1.0.0",
    "log_level": "INFO",
    "max_workers": 4,
    "timeout": 30,
    "retry_attempts": 3,
    "output_dir": "./output",
}


class ConfigLoader:
    """Loads configuration from JSON files and environment variables, merging with defaults."""

    def __init__(self, config_path: Optional[str] = None):
        self.config_path = Path(config_path) if config_path else None
        self._config: Dict[str, Any] = DEFAULT_CONFIG.copy()

    def load(self) -> Dict[str, Any]:
        """Load configuration from file and environment, applying overrides."""
        if self.config_path and self.config_path.exists():
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    file_config = json.load(f)
                    if isinstance(file_config, dict):
                        self._config.update(file_config)
            except (json.JSONDecodeError, OSError) as err:
                print(f"Warning: Failed to load config from {self.config_path}: {err}")

        self._apply_env_overrides()
        self._ensure_directories()
        return self._config

    def _apply_env_overrides(self) -> None:
        """Override settings using APP_ prefixed environment variables."""
        for key in self._config:
            env_key = f"APP_{key.upper()}"
            if env_key in os.environ:
                val = os.environ[env_key]
                default_val = DEFAULT_CONFIG.get(key)
                if isinstance(default_val, int):
                    try:
                        val = int(val)
                    except ValueError:
                        pass
                elif isinstance(default_val, bool):
                    val = val.lower() in ("true", "1", "yes")
                self._config[key] = val

    def _ensure_directories(self) -> None:
        """Ensure required directories exist."""
        out_dir = Path(self._config.get("output_dir", "./output"))
        out_dir.mkdir(parents=True, exist_ok=True)

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value by key."""
        return self._config.get(key, default)
