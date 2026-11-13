import json
import os
from typing import Any, Optional

def load_json_file(filepath: str) -> dict[str, Any]:
    """Loads data from a json file with error handling."""
    if not os.path.exists(filepath):
        return {}
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def save_json_file(filepath: str, data: dict[str, Any]) -> bool:
    """Saves a dictionary to a json file."""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def sanitize_dict(data: dict[str, Any]) -> dict[str, Any]:
    """Removes null values from a dictionary."""
    return {k: v for k, v in data.items() if v is not None}

def format_data_size(size_bytes: int) -> str:
    """Human readable string for byte sizes."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} TB"