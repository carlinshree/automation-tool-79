import json
import os
from datetime import datetime
from typing import Any, Dict, Optional

def load_json_config(file_path: str) -> Dict[str, Any]:
    """Load and parse a JSON configuration file."""
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json_config(file_path: str, data: Dict[str, Any]) -> None:
    """Save data dictionary to a JSON file."""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def get_timestamp_string() -> str:
    """Return current UTC timestamp as ISO string."""
    return datetime.utcnow().isoformat()

def safe_get(dictionary: Dict, key: str, default: Any = None) -> Any:
    """Safely retrieve value from nested dictionaries."""
    return dictionary.get(key, default)

def ensure_directory(path: str) -> None:
    """Create directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)