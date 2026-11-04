import functools
from typing import Any, Callable

# Cache for compute-intensive tasks
_memo_cache = {}

def memoize(func: Callable) -> Callable:
    """Decorator to cache function results to save cycles."""
    @functools.wraps(func)
    def wrapper(*args: Any) -> Any:
        if args not in _memo_cache:
            _memo_cache[args] = func(*args)
        return _memo_cache[args]
    return wrapper

class DataProcessor:
    def __init__(self, batch_size: int = 1000):
        self.batch_size = batch_size

    @memoize
    def transform(self, data: tuple) -> list:
        """Process data using batching optimization."""
        results = []
        # Simulate intensive processing logic
        for i in range(0, len(data), self.batch_size):
            batch = data[i:i + self.batch_size]
            results.extend([x * 2 for x in batch])
        return results

    def execute_pipeline(self, raw_data: list) -> list:
        """Pipeline entry point for efficient data handling."""
        if not raw_data:
            return []
        # Convert to tuple for hashability in memoization
        return self.transform(tuple(raw_data))

def clear_processor_cache() -> None:
    """Manual cache invalidation for memory management."""
    _memo_cache.clear()