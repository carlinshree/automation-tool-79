import re

def validate_input(data: dict) -> bool:
    """Validates mandatory keys and data formats."""
    required_keys = {'task_id', 'payload', 'priority'}
    
    # Check for missing keys
    if not all(key in data for key in required_keys):
        return False

    # Validate task_id format (alphanumeric string)
    if not isinstance(data['task_id'], str) or not re.match(r'^[A-Z0-9_-]+$', data['task_id']):
        return False

    # Validate priority range
    if not isinstance(data['priority'], int) or not (1 <= data['priority'] <= 5):
        return False

    return True

def sanitize_payload(payload: str) -> str:
    """Strip malicious characters from input string."""
    return re.sub(r'[^a-zA-Z0-9\s]', '', payload)

def process_with_validation(queue):
    """Main loop iteration with input validation."""
    for entry in queue:
        if not validate_input(entry):
            print(f"Skipping invalid task: {entry.get('task_id', 'unknown')}")
            continue
        
        # Process sanitized data
        clean_data = sanitize_payload(entry['payload'])
        print(f"Processing task {entry['task_id']} with priority {entry['priority']}: {clean_data}")