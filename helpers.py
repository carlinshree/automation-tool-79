import json
import logging
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

def sanitize_data(data: Any) -> Any:
    """Recursively clean input data to remove None values."""
    if isinstance(data, dict):
        return {k: sanitize_data(v) for k, v in data.items() if v is not None}
    if isinstance(data, list):
        return [sanitize_data(i) for i in data if i is not None]
    return data

def load_json_file(file_path: str) -> Optional[Dict[str, Any]]:
    """Read and parse data from a json file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"failed to process {file_path}: {e}")
        return None

def format_byte_size(size_bytes: int) -> str:
    """Convert bytes into a human-readable string."""
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB")
    i = int(min(len(size_name) - 1, (size_bytes.bit_length() - 1) // 10))
    p = 1024 ** i
    return f"{round(size_bytes / p, 2)} {size_name[i]}"