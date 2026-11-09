"""Data processing utilities for automation pipelines."""

from typing import Any, Dict, List, Optional


class BatchProcessor:
    """Processes datasets in configurable batches with optional transformation."""

    def __init__(self, batch_size: int = 100, drop_invalid: bool = True) -> None:
        """Initialize the processor with batch size and validation settings."""
        self.batch_size: int = max(1, batch_size)
        self.drop_invalid: bool = drop_invalid
        self.processed_count: int = 0
        self.errors: List[Dict[str, Any]] = []

    def validate_item(self, item: Dict[str, Any]) -> bool:
        """Check if an item contains required structure and non-empty key fields."""
        if not isinstance(item, dict):
            return False
        return bool(item.get("id") and "data" in item)

    def process_batch(self, items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Process a chunk of data items and collect error reports.

        Args:
            items: A list of record dictionaries to process.

        Returns:
            A list of successfully processed record dictionaries.
        """
        results: List[Dict[str, Any]] = []
        for index, item in enumerate(items):
            if not self.validate_item(item):
                self.errors.append({"index": index, "item": item, "reason": "Validation failed"})
                if self.drop_invalid:
                    continue

            transformed = self._transform_item(item)
            results.append(transformed)
            self.processed_count += 1

        return results

    def _transform_item(self, item: Dict[str, Any]) -> Dict[str, Any]:
        """Apply internal transformations to a single item."""
        cleaned = item.copy()
        cleaned["processed"] = True
        cleaned["status"] = str(cleaned.get("status", "pending")).upper()
        return cleaned

    def split_into_batches(self, items: List[Dict[str, Any]]) -> List[List[Dict[str, Any]]]:
        """Split a large list into uniform batch sizes."""
        return [items[i : i + self.batch_size] for i in range(0, len(items), self.batch_size)]
