import re
from datetime import datetime
from typing import Any, Dict, List, Sequence, TypeVar

T = TypeVar("T")


def get_timestamp(prefix: str = "", suffix: str = "") -> str:
    """Generate a standardized timestamp string for files or logs."""
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    parts = [p for p in (prefix, now, suffix) if p]
    return "_".join(parts)


def chunk_list(items: Sequence[T], chunk_size: int) -> List[Sequence[T]]:
    """Split a sequence into smaller lists of specified chunk size."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")
    return [items[i : i + chunk_size] for i in range(0, len(items), chunk_size)]


def deep_get(data: Dict[str, Any], path: str, default: Any = None) -> Any:
    """Retrieve nested values from a dictionary using dot notation (e.g., 'a.b.c')."""
    keys = path.split(".")
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current


def sanitize_filename(name: str, replacement: str = "_") -> str:
    """Sanitize string to be safe for filesystem usage."""
    cleaned = re.sub(r'[\\/*?:"<>|]', replacement, name)
    cleaned = re.sub(r"\s+", "_", cleaned)
    return cleaned.strip("_")
