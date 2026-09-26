import os
import time
from typing import Any, Callable, Dict, List, Tuple, Type


def ensure_directory(path: str) -> None:
    """Ensure that a directory exists, creating it if necessary."""
    if path:
        os.makedirs(path, exist_ok=True)


def safe_nested_get(
    data: Dict[str, Any], keys: List[str], default: Any = None
) -> Any:
    """Safely retrieve a nested value from a dictionary using a list of keys."""
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current


def chunk_list(data: List[Any], size: int) -> List[List[Any]]:
    """Split a list into smaller chunks of a specified maximum size."""
    if size <= 0:
        raise ValueError("Chunk size must be greater than zero.")
    return [data[i : i + size] for i in range(0, len(data), size)]


def retry_operation(
    func: Callable[..., Any],
    retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
    *args: Any,
    **kwargs: Any,
) -> Any:
    """Execute a function and retry it upon failure with exponential backoff."""
    current_delay = delay
    for attempt in range(retries):
        try:
            return func(*args, **kwargs)
        except exceptions as e:
            if attempt == retries - 1:
                raise e
            time.sleep(current_delay)
            current_delay *= backoff
