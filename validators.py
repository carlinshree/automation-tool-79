"""Input validation utilities for automation processing loop."""

from typing import Any, Dict, List, Optional, Tuple


class ValidationError(Exception):
    """Raised when processing input fails validation criteria."""
    pass


def validate_task_payload(data: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
    """Validate an individual task payload before processing."""
    if not isinstance(data, dict):
        return False, "Payload must be a dictionary"

    required_fields = ["id", "action", "params"]
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: '{field}'"

    if not isinstance(data["id"], (str, int)) or not str(data["id"]).strip():
        return False, "Task ID must be a non-empty string or integer"

    allowed_actions = ["clean", "transform", "export", "notify"]
    if data["action"] not in allowed_actions:
        return False, f"Invalid action '{data['action']}'. Must be one of {allowed_actions}"

    if not isinstance(data["params"], dict):
        return False, "Params field must be a dictionary"

    return True, None


def validate_batch_input(batch: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Validate a batch of task inputs, returning only valid items."""
    if not isinstance(batch, list):
        raise ValidationError("Batch input must be a list of task objects")

    valid_items = []
    for index, item in enumerate(batch):
        is_valid, error_msg = validate_task_payload(item)
        if is_valid:
            valid_items.append(item)
        else:
            # Skip invalid items during processing loop
            continue

    return valid_items
