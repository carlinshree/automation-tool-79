import os
import json
import logging
from typing import Any, Dict

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('automation-tool-79')

def load_json(filepath: str) -> Dict[str, Any]:
    """Load and parse a JSON configuration file."""
    if not os.path.exists(filepath):
        logger.error(f"file not found: {filepath}")
        return {}
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        logger.error(f"invalid json format: {e}")
        return {}

def ensure_dir(directory: str) -> None:
    """Create directory path if it does not exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)
        logger.info(f"directory created: {directory}")

def get_env_var(key: str, default: Any = None) -> Any:
    """Fetch environment variable with fallback."""
    return os.environ.get(key, default)

def sanitize_filename(name: str) -> str:
    """Remove problematic characters from string."""
    return "".join([c if c.isalnum() else "_" for c in name])