import logging
import sys
from typing import Any, Dict, Optional

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

logger = logging.getLogger("automation-tool-79")


class AutomationError(Exception):
    """Base exception for automation-tool-79 execution errors."""
    pass


def process_payload(payload: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    """Process input payload with robust error handling for edge cases."""
    if payload is None:
        logger.warning("Received null payload, returning empty result structure.")
        return {"status": "skipped", "data": {}}

    if not isinstance(payload, dict):
        logger.error(f"Invalid payload type received: {type(payload).__name__}")
        raise AutomationError(f"Expected dict payload, got {type(payload).__name__}")

    try:
        target_key = payload.get("action")
        if not target_key:
            raise ValueError("Missing required 'action' field in payload")
            
        logger.info(f"Successfully processed action: {target_key}")
        return {"status": "success", "action": target_key, "data": payload.get("data", {})}
        
    except ValueError as ve:
        logger.error(f"Validation error during processing: {ve}")
        return {"status": "error", "message": str(ve)}
    except Exception as exc:
        logger.critical(f"Unexpected error encountered: {exc}", exc_info=True)
        raise AutomationError(f"Critical failure in process_payload: {exc}") from exc
