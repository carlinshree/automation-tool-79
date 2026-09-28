import re
from typing import Any, Optional

class DataValidator:
    """Utility class for payload schema validation."""

    EMAIL_PATTERN = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

    @staticmethod
    def is_valid_email(email: Any) -> bool:
        """Checks if the provided input is a valid email string."""
        if not isinstance(email, str):
            return False
        return bool(DataValidator.EMAIL_PATTERN.match(email))

    @staticmethod
    def validate_range(value: int, min_val: int, max_val: int) -> bool:
        """Ensures value falls within the specified inclusive range."""
        return min_val <= value <= max_val

    @staticmethod
    def sanitize_input(data: Optional[str]) -> str:
        """Strips whitespace and ensures data is a string."""
        return str(data).strip() if data else ""

    @classmethod
    def validate_payload(cls, data: dict, required_keys: list) -> bool:
        """Verifies that all required keys are present in the dictionary."""
        return all(key in data for key in required_keys)
