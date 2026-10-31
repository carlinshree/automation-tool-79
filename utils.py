"""Utility functions for general data manipulation and transformation."""

from typing import Any, Dict, List, Union


def flatten_dict(
    d: Dict[str, Any], parent_key: str = "", sep: str = "."
) -> Dict[str, Any]:
    """Flatten a deeply nested dictionary using a separator for keys."""
    items: List[tuple] = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            for i, item in enumerate(v):
                if isinstance(item, dict):
                    items.extend(
                        flatten_dict(item, f"{new_key}{sep}{i}", sep=sep).items()
                    )
                else:
                    items.append((f"{new_key}{sep}{i}", item))
        else:
            items.append((new_key, v))
    return dict(items)


def deep_get(data: Dict[str, Any], path: str, default: Any = None, sep: str = ".") -> Any:
    """Safely retrieve a value from a nested dictionary using a dot-separated path."""
    keys = path.split(sep)
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        elif isinstance(current, list) and key.isdigit():
            idx = int(key)
            if 0 <= idx < len(current):
                current = current[idx]
            else:
                return default
        else:
            return default
    return current


def batch_iterable(data_list: List[Any], batch_size: int) -> List[List[Any]]:
    """Split a list or iterable into smaller chunks of specified size."""
    if batch_size <= 0:
        raise ValueError("batch_size must be greater than zero")
    return [data_list[i : i + batch_size] for i in range(0, len(data_list), batch_size)]
