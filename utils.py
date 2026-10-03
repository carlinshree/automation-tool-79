import json
from typing import Any, Dict, Optional

def load_json_file(file_path: str) -> Optional[Dict[str, Any]]:
    """
    Reads and parses a JSON file safely.
    Returns dictionary if successful, None otherwise.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, IOError):
        return None

def save_json_file(data: Dict[str, Any], file_path: str) -> bool:
    """
    Serializes data to a JSON file with pretty printing.
    Returns True on success, False on failure.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, sort_keys=True)
        return True
    except (TypeError, IOError):
        return False

def sanitize_input(data: Any) -> Any:
    """
    Basic stripping of string inputs for cleaner processing.
    """
    if isinstance(data, str):
        return data.strip()
    if isinstance(data, dict):
        return {k: sanitize_input(v) for k, v in data.items()}
    if isinstance(data, list):
        return [sanitize_input(i) for i in data]
    return data