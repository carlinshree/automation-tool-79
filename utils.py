import os
from typing import List, Optional, Union

def load_environment_variable(key: str, default: Optional[str] = None) -> str:
    """Retrieve an environment variable or return a fallback default."""
    return os.getenv(key, default) or ""

def format_file_path(base_path: str, *parts: str) -> str:
    """Construct a standardized file path from multiple segments."""
    return os.path.normpath(os.path.join(base_path, *parts))

def split_list_by_chunk_size(items: List[Union[str, int]], size: int) -> List[List[Union[str, int]]:
    """Divide a list into smaller sub-lists of a defined length."""
    if size <= 0:
        raise ValueError("Chunk size must be greater than zero.")
    return [items[i:i + size] for i in range(0, len(items), size)]

def validate_directory_exists(path: str) -> bool:
    """Check if the provided path is a directory and exists."""
    return os.path.isdir(path)

def sanitize_input_string(value: str) -> str:
    """Remove whitespace and normalize line endings for processing."""
    return value.strip().replace('\r\n', '\n')
