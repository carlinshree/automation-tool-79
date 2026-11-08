import json
import os
from typing import Any, Dict, Optional

def load_json_file(file_path: str) -> Dict[str, Any]:
    """Loads data from a json file with existence checks."""
    if not os.path.exists(file_path):
        return {}
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def save_json_file(file_path: str, data: Dict[str, Any]) -> bool:
    """Writes dictionary data to a json file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def sanitize_dict_keys(data: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively ensures all dictionary keys are strings."""
    new_data = {}
    for key, value in data.items():
        new_key = str(key)
        if isinstance(value, dict):
            new_data[new_key] = sanitize_dict_keys(value)
        else:
            new_data[new_key] = value
    return new_data

def get_nested_value(data: Dict[str, Any], path: str, delimiter: str = '.') -> Optional[Any]:
    """Retrieves value from nested dictionary using path string."""
    keys = path.split(delimiter)
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return None
    return current