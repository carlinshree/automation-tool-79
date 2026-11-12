import re
from typing import Any, Optional

def validate_input_data(data: dict) -> bool:
    """Ensures dictionary contains required fields and valid formats."""
    required_keys = {'task_id', 'priority', 'payload'}
    if not all(key in data for key in required_keys):
        return False
    
    # Validate task_id pattern and priority range
    if not re.match(r'^[a-zA-Z0-9_-]+$', str(data['task_id'])):
        return False
    
    if not isinstance(data['priority'], int) or not (1 <= data['priority'] <= 5):
        return False
        
    return True

def process_main_loop(items: list[dict]) -> None:
    """Main loop processing with input sanitization."""
    for item in items:
        if not isinstance(item, dict):
            continue
            
        if validate_input_data(item):
            print(f"Processing task: {item['task_id']}")
        else:
            print(f"Skipping invalid task: {item.get('task_id', 'unknown')}")

def sanitize_string(value: Any) -> str:
    """Converts input to clean string for log compatibility."""
    if value is None:
        return ""
    return str(value).strip()[:255]