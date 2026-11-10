import json
import os
from datetime import datetime
from typing import Any, Dict, Optional

def load_json(filepath: str) -> Dict[str, Any]:
    """Load configuration from a JSON file."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(filepath: str, data: Dict[str, Any]) -> None:
    """Save dictionary data to a JSON file."""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

def get_timestamp() -> str:
    """Return current ISO formatted timestamp."""
    return datetime.now().isoformat()

def ensure_dir(directory: str) -> None:
    """Create directory if it does not exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def sanitize_filename(filename: str) -> str:
    """Basic sanitization for safe file names."""
    return "".join([c for c in filename if c.isalnum() or c in (' ', '.', '_')]).rstrip()
