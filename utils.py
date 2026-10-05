import json
import os
from datetime import datetime
from typing import Any, Dict, Optional

def load_json(filepath: str) -> Dict[str, Any]:
    """Load and parse a JSON file safely."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(filepath: str, data: Dict[str, Any]) -> None:
    """Save dictionary to a formatted JSON file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def get_timestamp() -> str:
    """Return current ISO formatted timestamp."""
    return datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

def ensure_directory(path: str) -> None:
    """Create directory path if it missing."""
    if not os.path.exists(path):
        os.makedirs(path)

def sanitize_filename(filename: str) -> str:
    """Replace spaces and special characters."""
    return "".join(c if c.isalnum() else '_' for c in filename).lower()

def log_event(message: str, level: str = "INFO") -> None:
    """Standard output formatting for automation logs."""
    timestamp = get_timestamp()
    print(f"[{timestamp}] {level}: {message}")