import logging
from typing import Any, Dict, List, Tuple

logger = logging.getLogger(__name__)


def validate_payload(item: Dict[str, Any]) -> Tuple[bool, str]:
    """Validate an individual item payload before processing."""
    if not isinstance(item, dict):
        return False, "Item must be a dictionary"
    
    if "id" not in item or not item["id"]:
        return False, "Missing or empty 'id' field"
    
    if "task" not in item or not isinstance(item["task"], str):
        return False, "Invalid or missing 'task' string"
    
    if "data" in item and not isinstance(item["data"], (dict, list)):
        return False, "'data' field must be a dict or list"
    
    return True, ""


def process_queue(queue: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    """Process queue items with strict input validation in the main loop."""
    summary: Dict[str, List[Dict[str, Any]]] = {"completed": [], "rejected": []}

    for item in queue:
        is_valid, reason = validate_payload(item)
        if not is_valid:
            logger.warning("Rejecting invalid item: %s", reason)
            summary["rejected"].append({"item": item, "reason": reason})
            continue

        try:
            item_id = str(item["id"])
            task = item["task"].strip().lower()
            payload = item.get("data", {})

            # Execute task payload handling
            result = {"id": item_id, "task": task, "status": "executed", "payload": payload}
            summary["completed"].append(result)
        except Exception as err:
            logger.error("Error executing task for item %s: %s", item.get("id"), err)
            summary["rejected"].append({"item": item, "reason": str(err)})

    return summary
