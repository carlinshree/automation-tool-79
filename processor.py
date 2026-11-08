import concurrent.futures
from functools import lru_cache
from typing import Any, Callable, Iterable, List


class BatchProcessor:
    """Optimized concurrent batch processor for automated tasks."""

    def __init__(self, max_workers: int = 4, chunk_size: int = 100):
        self.max_workers = max_workers
        self.chunk_size = chunk_size

    @lru_cache(maxsize=1024)
    def _cached_transform(self, item: str) -> str:
        """Cached helper to eliminate redundant string normalization."""
        return item.strip().lower()

    def _chunk_iterable(self, items: Iterable[Any]) -> Iterable[List[Any]]:
        """Yield successive chunks from input iterable to optimize memory usage."""
        chunk = []
        for item in items:
            chunk.append(item)
            if len(chunk) == self.chunk_size:
                yield chunk
                chunk = []
        if chunk:
            yield chunk

    def process_items(
        self, items: List[Any], func: Callable[[Any], Any]
    ) -> List[Any]:
        """Process items concurrently in chunked batches to improve throughput."""
        if not items:
            return []

        results: List[Any] = []
        prepared_items = [
            self._cached_transform(item) if isinstance(item, str) else item
            for item in items
        ]

        with concurrent.futures.ThreadPoolExecutor(
            max_workers=self.max_workers
        ) as executor:
            for chunk in self._chunk_iterable(prepared_items):
                chunk_results = list(executor.map(func, chunk))
                results.extend(chunk_results)

        return results
