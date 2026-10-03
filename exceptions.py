from typing import Optional

class AutomationError(Exception):
    """Base exception class for automation-tool-79."""
    def __init__(self, message: str, code: Optional[int] = None) -> None:
        super().__init__(message)
        self.code = code

class ConfigurationError(AutomationError):
    """Raised when configuration validation fails."""
    pass

class ExecutionError(AutomationError):
    """Raised when an automation task fails during execution."""
    def __init__(self, message: str, task_id: str, code: Optional[int] = None) -> None:
        super().__init__(message, code)
        self.task_id = task_id

class ValidationError(AutomationError):
    """Raised when data inputs fail schema checks."""
    pass

def format_error(error: AutomationError) -> str:
    """Return a formatted string representation of an error."""
    if isinstance(error, ExecutionError):
        return f"Task {error.task_id} failed: {error} (Code: {error.code})"
    return f"Error: {error}"