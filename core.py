import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Callable, Any, Dict, List, Optional


class TaskRunner:
    """Core execution engine optimized for parallel batch automation tasks."""

    def __init__(self, max_workers: int = 4):
        self.max_workers = max_workers
        self._cache: Dict[str, Any] = {}

    @staticmethod
    def _generate_key(func_name: str, args: tuple, kwargs: dict) -> str:
        """Generate a unique deterministic cache key for task arguments."""
        kwargs_str = ",".join(f"{k}={v}" for k, v in sorted(kwargs.items()))
        return f"{func_name}:{args}:{kwargs_str}"

    def execute_cached(self, func: Callable, *args: Any, **kwargs: Any) -> Any:
        """Execute a single function with result caching to prevent redundant work."""
        key = self._generate_key(func.__name__, args, kwargs)
        if key in self._cache:
            return self._cache[key]

        result = func(*args, **kwargs)
        self._cache[key] = result
        return result

    def run_batch(self, items: List[Any], task_fn: Callable[[Any], Any], use_cache: bool = True) -> List[Any]:
        """Process a list of items concurrently using thread pooling."""
        if not items:
            return []

        results = [None] * len(items)

        def worker(index: int, item: Any) -> tuple:
            if use_cache:
                res = self.execute_cached(task_fn, item)
            else:
                res = task_fn(item)
            return index, res

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [executor.submit(worker, i, item) for i, item in enumerate(items)]
            for future in as_completed(futures):
                idx, result = future.result()
                results[idx] = result

        return results

    def clear_cache(self) -> None:
        """Clear the internal task result cache."""
        self._cache.clear()
