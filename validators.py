import re
from typing import Any, Optional

class InputValidator:
    """Utility for data integrity in automation-tool-79 processing loops."""

    @staticmethod
    def validate_task_id(task_id: Any) -> bool:
        """Ensures task ID is a non-empty alphanumeric string."""
        if not isinstance(task_id, str):
            return False
        return bool(re.fullmatch(r'[a-zA-Z0-9_-]+', task_id))

    @staticmethod
    def validate_payload(data: dict) -> bool:
        """Checks for required keys in the automation payload."""
        required_keys = {'action', 'target', 'priority'}
        if not isinstance(data, dict):
            return False
        return required_keys.issubset(data.keys())

    @staticmethod
    def sanitize_input(value: str) -> str:
        """Strips potential shell injection characters."""
        return re.sub(r'[^a-zA-Z0-9_\-\.]', '', value)

def process_input(data: dict) -> Optional[dict]:
    """Main entry point for loop validation."""
    validator = InputValidator()

    if not validator.validate_payload(data):
        return None

    if not validator.validate_task_id(data.get('task_id', '')):
        return None

    return {
        'action': validator.sanitize_input(data['action']),
        'target': validator.sanitize_input(data['target']),
        'priority': int(data['priority'])
    }