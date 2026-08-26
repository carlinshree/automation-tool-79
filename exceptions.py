class AutomationError(Exception):
    """Base exception for automation-tool-79 errors."""
    pass


class ConfigurationError(AutomationError):
    """Raised when configuration settings are invalid or missing."""
    def __init__(self, message: str, key: str = None):
        super().__init__(message)
        self.key = key


class ProcessingError(AutomationError):
    """Raised when data processing encounters an unexpected edge case."""
    def __init__(self, message: str, status_code: int = 500):
        super().__init__(message)
        self.status_code = status_code


class ValidationError(AutomationError):
    """Raised when input validation fails for critical tasks."""
    def __init__(self, message: str, errors: list = None):
        super().__init__(message)
        self.errors = errors or []


def handle_exception(exc: Exception) -> dict:
    """Convert caught exceptions into a standardized response format."""
    if isinstance(exc, AutomationError):
        return {
            "error": exc.__class__.__name__,
            "message": str(exc),
            "details": getattr(exc, 'errors', getattr(exc, 'key', None))
        }
    return {
        "error": "UnexpectedError",
        "message": str(exc),
        "details": None
    }
