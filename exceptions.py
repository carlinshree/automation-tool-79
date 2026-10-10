from typing import Optional

class AutomationError(Exception):
    """Base exception class for automation-tool-79."""
    def __init__(self, message: str, code: Optional[int] = None) -> None:
        super().__init__(message)
        self.code = code

class ConfigurationError(AutomationError):
    """Raised when tool configuration is invalid or missing."""
    pass

class ExecutionError(AutomationError):
    """Raised when a primary task process fails."""
    def __init__(self, message: str, task_id: str, code: Optional[int] = None) -> None:
        super().__init__(message, code)
        self.task_id = task_id

class ValidationError(AutomationError):
    """Raised during data integrity validation checks."""
    def __init__(self, message: str, field: str) -> None:
        super().__init__(f"{field}: {message}")
        self.field = field

class TimeoutError(AutomationError):
    """Raised when an operation exceeds allowed duration."""
    def __init__(self, message: str, duration: float) -> None:
        super().__init__(f"{message} (limit: {duration}s)")
        self.duration = duration