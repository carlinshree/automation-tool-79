import re
from typing import Any, Dict, Optional

def validate_input(data: Dict[str, Any]) -> bool:
    """Checks if input data meets schema requirements."""
    required_keys = {'id', 'task', 'priority'}
    
    # Verify all required keys exist
    if not all(key in data for key in required_keys):
        return False

    # Validate id format (alphanumeric)
    if not isinstance(data['id'], str) or not re.match(r'^[a-zA-Z0-9]+$', data['id']):
        return False

    # Validate priority range
    if not isinstance(data['priority'], int) or not (1 <= data['priority'] <= 10):
        return False

    return True

def sanitize_task_name(task_name: str) -> str:
    """Removes dangerous characters from task descriptions."""
    return re.sub(r'[^a-zA-Z0-9\s_-]', '', task_name).strip()

def process_payload(payload: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    """Standardizes and validates input payload for the processor."""
    if not payload or not validate_input(payload):
        raise ValueError("invalid input structure detected")

    return {
        "id": payload['id'],
        "task": sanitize_task_name(payload['task']),
        "priority": payload['priority']
    }