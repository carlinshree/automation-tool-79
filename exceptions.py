class AutomationError(Exception):
    """Base exception for automation-tool-79."""
    pass

class ValidationError(AutomationError):
    """Raised when input validation fails."""
    pass

class ProcessingError(AutomationError):
    """Raised when data transformation fails."""
    pass

class ConfigurationError(AutomationError):
    """Raised for missing or invalid config."""
    pass

def handle_automation_errors(func):
    """Decorator for centralized error catching."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except AutomationError as e:
            print(f"Caught expected error: {e}")
            raise
        except Exception as e:
            print(f"Caught unexpected system failure: {e}")
            raise RuntimeError("Fatal processing failure") from e
    return wrapper

# Usage example:
# @handle_automation_errors
# def execute_task():
#     raise ValidationError("Invalid parameter provided")