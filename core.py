import concurrent.futures
import functools
import hashlib
from typing import Any, Callable, Dict, List


class ExecutionCore:
    """Core execution engine optimized for batch task processing and caching."""

    def __init__(self, max_workers: int = 4):
        self.max_workers = max_workers
        self._result_cache: Dict[str, Any] = {}

    @functools.lru_cache(maxsize=128)
    def compute_hash(self, data: str) -> str:
        """Cached helper for computing lightweight task fingerprints."""
        return hashlib.sha256(data.encode('utf-8')).hexdigest()

    def process_item_fast(self, item: Dict[str, Any], task_fn: Callable) -> Dict[str, Any]:
        """Process a single item using cached computation where possible."""
        item_id = str(item.get('id', ''))
        cache_key = f"{item_id}:{item.get('payload', '')}"
        fingerprint = self.compute_hash(cache_key)

        if fingerprint in self._result_cache:
            return {'id': item_id, 'result': self._result_cache[fingerprint], 'cached': True}

        result = task_fn(item)
        self._result_cache[fingerprint] = result
        return {'id': item_id, 'result': result, 'cached': False}

    def run_batch_parallel(self, items: List[Dict[str, Any]], task_fn: Callable) -> List[Dict[str, Any]]:
        """Execute a batch of automation tasks concurrently to improve throughput."""
        if not items:
            return []

        results = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [
                executor.submit(self.process_item_fast, item, task_fn)
                for item in items
            ]
            for future in concurrent.futures.as_completed(futures):
                try:
                    results.append(future.result())
                except Exception as err:
                    results.append({'error': str(err), 'status': 'failed'})

        return results

    def clear_cache(self) -> None:
        """Purge cached task results to release memory."""
        self._result_cache.clear()
        self.compute_hash.cache_clear()
