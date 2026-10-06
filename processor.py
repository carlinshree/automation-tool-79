import logging
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

class DataProcessor:
    """Handles core data transformation for automation-tool-79."""
    
    def process_item(self, data: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        # validation of input structure
        if not isinstance(data, dict):
            logger.error("Invalid input type: expected dictionary")
            raise ValueError("Input must be a dictionary")

        try:
            # edge case: missing required fields
            result = {
                "id": data.get("id"),
                "status": "processed",
                "payload": data.get("payload", {})
            }
            
            if result["id"] is None:
                raise KeyError("Missing mandatory key: id")

            return result
            
        except KeyError as e:
            logger.warning(f"Data processing failure: {e}")
            return {"status": "error", "error": str(e)}
            
        except Exception as e:
            logger.critical(f"Unexpected system failure: {e}", exc_info=True)
            return {"status": "failed", "error": "internal processing error"}

if __name__ == "__main__":
    proc = DataProcessor()
    print(proc.process_item({"id": 1, "payload": "data"}))