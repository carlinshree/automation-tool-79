import os
from typing import Any, Dict

# Default configuration settings for automation-tool-79
DEFAULT_CONFIG: Dict[str, Any] = {
    "app_name": "automation-tool-79",
    "environment": "development",
    "timeout_seconds": 30,
    "max_retries": 3,
    "log_level": "INFO",
    "storage_path": "./data",
}


def load_configuration(override_path: str = None) -> Dict[str, Any]:
    """Load configuration by merging defaults with environment variables."""
    config = DEFAULT_CONFIG.copy()

    # Override with environment variables if present
    for key in config.keys():
        env_key = f"TOOL_{key.upper()}"
        if env_key in os.environ:
            val = os.environ[env_key]
            # Basic type casting for standard config types
            if isinstance(config[key], int):
                val = int(val)
            elif isinstance(config[key], bool):
                val = val.lower() in ("true", "1", "yes")
            config[key] = val

    # Handle direct override path if specified
    if override_path and os.path.exists(override_path):
        # Simple key-value file parser placeholder logic
        with open(override_path, "r") as f:
            for line in f:
                if "=" in line and not line.startswith("#"):
                    k, v = line.strip().split("=", 1)
                    if k.lower() in config:
                        config[k.lower()] = v.strip()

    return config
