from typing import List, Dict, Optional, Any

class DataProcessor:
    """Handles transformation of raw data batches."""

    def __init__(self, settings: Optional[Dict[str, Any]] = None) -> None:
        self.settings = settings or {}
        self.buffer: List[str] = []

    def ingest(self, item: str) -> None:
        """Adds a string item to the processing buffer."""
        if item:
            self.buffer.append(item.strip())

    def process_batch(self, threshold: int = 5) -> List[str]:
        """Transforms and clears buffer if threshold reached."""
        if len(self.buffer) < threshold:
            return []

        processed = [item.upper() for item in self.buffer]
        self.buffer.clear()
        return processed

    def get_status(self) -> Dict[str, int]:
        """Returns current state of the processor."""
        return {"buffered_count": len(self.buffer)}

def run_pipeline(data: List[str]) -> List[str]:
    """Utility function to execute a full pass."""
    processor = DataProcessor()
    for entry in data:
        processor.ingest(entry)
    return processor.process_batch(threshold=0)