"""Helper functions for common automation tasks."""

import time
from typing import Callable, Any, List, TypeVar

T = TypeVar("T")


def retry_operation(
    func: Callable[..., T],
    retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    *args: Any,
    **kwargs: Any
) -> T:
    """Retry a function call with exponential backoff on failure."""
    current_delay = delay
    for attempt in range(1, retries + 1):
        try:
            return func(*args, **kwargs)
        except Exception as err:
            if attempt == retries:
                raise err
            time.sleep(current_delay)
            current_delay *= backoff


def chunk_list(items: List[T], chunk_size: int) -> List[List[T]]:
    """Split a list into smaller chunks of specified size."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero")
    return [items[i : i + chunk_size] for i in range(0, len(items), chunk_size)]


def flatten_dict(d: dict, parent_key: str = "", sep: str = ".") -> dict:
    """Flatten a nested dictionary into a single-level dictionary."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else str(k)
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)
