from typing import List, Dict, Any, Optional

class DataHandler:
    """Manages processing of incoming data streams."""

    def __init__(self, target_id: str, timeout: int = 30) -> None:
        self.target_id = target_id
        self.timeout = timeout
        self.buffer: List[Dict[str, Any]] = []

    def add_entry(self, data: Dict[str, Any]) -> bool:
        """Adds a new entry to the internal buffer."""
        if not isinstance(data, dict):
            return False
        self.buffer.append(data)
        return True

    def get_summary(self) -> Dict[str, Any]:
        """Returns a summary dictionary of current buffer state."""
        return {
            "target": self.target_id,
            "count": len(self.buffer),
            "status": "active" if self.timeout > 0 else "idle"
        }

    def clear_buffer(self, filter_key: Optional[str] = None) -> int:
        """Clears buffer entries and returns count of removed items."""
        initial_count = len(self.buffer)
        if filter_key:
            self.buffer = [item for item in self.buffer if filter_key not in item]
        else:
            self.buffer.clear()
        return initial_count - len(self.buffer)