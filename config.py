import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "app_name": "automation-tool-79",
    "timeout": 30,
    "retries": 3,
    "debug_mode": False,
    "log_level": "INFO",
}

def load_configuration(override_path: str = None) -> Dict[str, Any]:
    """
    Load configuration with fallback to default values.
    Reads environment variables if present to override defaults.
    """
    config = DEFAULT_CONFIG.copy()
    
    # Environment variable override mechanism
    for key in config.keys():
        env_key = f"AUTO79_{key.upper()}"
        if env_key in os.environ:
            val = os.environ[env_key]
            # Basic type casting based on default value type
            default_val = config[key]
            if isinstance(default_val, bool):
                config[key] = val.lower() in ("true", "1", "yes")
            elif isinstance(default_val, int):
                try:
                    config[key] = int(val)
                except ValueError:
                    pass
            else:
                config[key] = val
                
    return config

if __name__ == "__main__":
    cfg = load_configuration()
    print(f"Loaded config for {cfg['app_name']}")