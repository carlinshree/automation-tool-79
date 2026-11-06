from typing import List, Optional, Union
import os

def get_file_list(directory: str, extension: str = ".txt") -> List[str]:
    """Retrieve filtered list of files from a directory."""
    if not os.path.exists(directory):
        return []

    files = [f for f in os.listdir(directory) if f.endswith(extension)]
    return sorted(files)

def format_data_size(size_bytes: Union[int, float]) -> str:
    """Convert bytes into a human-readable string format."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} TB"

def sanitize_input(value: Optional[str]) -> str:
    """Clean string input by stripping whitespace and handling None."""
    if value is None:
        return ""
    return value.strip().replace("\t", " ")

def validate_path(path: str) -> bool:
    """Check if provided path is valid and accessible."""
    return os.path.isabs(path) and os.path.exists(os.path.dirname(path))