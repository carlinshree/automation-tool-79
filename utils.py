from typing import Any, Dict, Generator, List


def flatten_dict(
    d: Dict[str, Any], parent_key: str = "", sep: str = "."
) -> Dict[str, Any]:
    """Recursively flatten a nested dictionary using key separators."""
    items: List[tuple] = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def deep_merge(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merge two dictionaries, overriding dict1 with dict2 values."""
    merged = dict1.copy()
    for key, value in dict2.items():
        if (
            key in merged
            and isinstance(merged[key], dict)
            and isinstance(value, dict)
        ):
            merged[key] = deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged


def chunk_list(data: List[Any], chunk_size: int) -> Generator[List[Any], None, None]:
    """Yield successive n-sized chunks from a list."""
    if chunk_size <= 0:
        raise ValueError("Chunk size must be greater than zero.")
    for i in range(0, len(data), chunk_size):
        yield data[i : i + chunk_size]


def sanitize_keys(
    d: Dict[str, Any], strip_whitespace: bool = True, lowercase: bool = False
) -> Dict[str, Any]:
    """Recursively sanitize dictionary keys by stripping whitespace or lowercasing."""
    cleaned: Dict[str, Any] = {}
    for key, value in d.items():
        new_key = key.strip() if strip_whitespace else key
        if lowercase:
            new_key = new_key.lower()
        if isinstance(value, dict):
            cleaned[new_key] = sanitize_keys(value, strip_whitespace, lowercase)
        else:
            cleaned[new_key] = value
    return cleaned
