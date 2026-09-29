from typing import List, Dict, Any, Optional
import json

def load_config(file_path: str) -> Dict[str, Any]:
    """Load configuration from a JSON file into a dictionary."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def format_data(items: List[str], prefix: str = "ID-") -> List[str]:
    """Apply a prefix to each item in the provided list."""
    return [f"{prefix}{item}" for item in items]

def filter_by_key(data: List[Dict[str, Any]], key: str, value: Any) -> List[Dict[str, Any]]:
    """Return entries from the list that match the specified key-value pair."""
    return [entry for entry in data if entry.get(key) == value]

def get_summary(data: List[int]) -> Optional[Dict[str, float]]:
    """Calculate basic statistics for a list of integers."""
    if not data:
        return None
    return {
        "avg": sum(data) / len(data),
        "max": float(max(data)),
        "min": float(min(data))
    }