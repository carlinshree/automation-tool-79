from typing import Dict, List, Any, Optional

class DataHandler:
    """Handles incoming data payloads for automation-tool-79."""

    def __init__(self, target_node: str, timeout: int = 30) -> None:
        self.target_node = target_node
        self.timeout = timeout
        self.buffer: List[Dict[str, Any]] = []

    def validate_payload(self, payload: Dict[str, Any]) -> bool:
        """Checks if payload contains required identifiers."""
        return "id" in payload and "data" in payload

    def process_entry(self, entry: Dict[str, Any]) -> Optional[str]:
        """Parses a single entry and stores it in the buffer."""
        if not self.validate_payload(entry):
            return None
        
        self.buffer.append(entry)
        return entry.get("id")

    def flush_buffer(self) -> int:
        """Clears the internal buffer and returns entry count."""
        count = len(self.buffer)
        self.buffer.clear()
        return count

    def get_status(self) -> Dict[str, Any]:
        """Returns the current state of the handler."""
        return {
            "node": self.target_node,
            "queued": len(self.buffer),
            "timeout": self.timeout
        }