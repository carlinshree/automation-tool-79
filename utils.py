from typing import List, Optional, Any
import os

def get_file_list(directory: str, extension: str = ".txt") -> List[str]:
    """Retrieve a list of files with a specific extension from a directory."""
    if not os.path.exists(directory):
        return []
    
    files = [f for f in os.listdir(directory) if f.endswith(extension)]
    return files

def format_payload(data: Any, prefix: str = "LOG") -> str:
    """Format data into a string with a standardized prefix."""
    return f"[{prefix}] {str(data).strip()}"

def safe_get_env(key: str, default: Optional[str] = None) -> Optional[str]:
    """Retrieve environment variables with an optional fallback."""
    return os.environ.get(key, default)

def parse_bool(value: Any) -> bool:
    """Convert input to boolean based on truthy checks."""
    if isinstance(value, bool):
        return value
    return str(value).lower() in ("true", "1", "yes", "on")