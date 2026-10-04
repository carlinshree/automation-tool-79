import json
import os
from typing import Any, Optional

def load_json_file(file_path: str) -> Optional[dict]:
    """Loads data from a local JSON file."""
    if not os.path.exists(file_path):
        return None
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return None

def save_json_file(file_path: str, data: Any) -> bool:
    """Persists dictionary data to a JSON file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except (TypeError, IOError):
        return False

def sanitize_input(data: str) -> str:
    """Cleans basic whitespace and newline characters."""
    return data.strip().replace('\n', '').replace('\r', '')

def format_data_bytes(size_in_bytes: int) -> str:
    """Converts raw byte count to readable string."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_in_bytes < 1024:
            return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= 1024
    return f"{size_in_bytes:.2f} TB"