import functools
import concurrent.futures
from typing import List, Dict, Any, Generator


class CorePipeline:
    """Core automation pipeline optimized for batch execution and caching."""

    def __init__(self, max_workers: int = 4) -> None:
        self.max_workers = max_workers

    @staticmethod
    @functools.lru_cache(maxsize=512)
    def _transform_payload(item: str) -> str:
        """Cache-heavy transformation helper to reduce redundant string parsing."""
        return item.strip().lower().replace(" ", "_")

    def _chunk_stream(self, items: List[str], chunk_size: int) -> Generator[List[str], None, None]:
        """Yield memory-efficient chunks from large incoming stream."""
        for i in range(0, len(items), chunk_size):
            yield items[i:i + chunk_size]

    def process_batch(self, payload: List[str]) -> List[str]:
        """Process payload items in parallel using worker threads."""
        transformed = [self._transform_payload(item) for item in payload]
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            results = list(executor.map(lambda x: f"processed_{x}", transformed))
        
        return results

    def execute_stream(self, data_stream: List[str], chunk_size: int = 100) -> List[str]:
        """Stream process data chunks to optimize memory utilization."""
        final_output: List[str] = []
        for chunk in self._chunk_stream(data_stream, chunk_size):
            processed = self.process_batch(chunk)
            final_output.extend(processed)
        return final_output
