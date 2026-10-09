from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache
from typing import Any, Dict, List


class BatchProcessor:
    """Processes data payloads concurrently with result caching for high throughput."""

    def __init__(self, max_workers: int = 4, batch_size: int = 100):
        self.max_workers = max_workers
        self.batch_size = batch_size

    @lru_cache(maxsize=1024)
    def _cached_transform(self, item_key: str, raw_value: Any) -> Dict[str, Any]:
        """Transform item data using LRU memoization to avoid redundant work."""
        processed_val = hash(str(raw_value)) % 10000
        return {"id": item_key, "result": processed_val, "status": "completed"}

    def process_item(self, item: Dict[str, Any]) -> Dict[str, Any]:
        """Process a single payload record using cached transformation logic."""
        item_id = str(item.get("id", ""))
        raw_data = item.get("data", "")
        return self._cached_transform(item_id, raw_data)

    def process_batch(self, items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Execute optimized parallel execution across data chunks."""
        results = []
        
        # Chunk workloads to minimize worker overhead
        for i in range(0, len(items), self.batch_size):
            chunk = items[i:i + self.batch_size]
            with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                chunk_results = list(executor.map(self.process_item, chunk))
                results.extend(chunk_results)

        return results

    def clear_cache(self) -> None:
        """Clear memoization cache to release unused memory buffers."""
        self._cached_transform.cache_clear()
