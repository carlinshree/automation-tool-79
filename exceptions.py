class AutomationError(Exception):
    """Base exception for automation-tool-79."""
    pass

class ConfigurationError(AutomationError):
    """Raised when settings are invalid."""
    pass

class ExecutionTimeoutError(AutomationError):
    """Raised when a process exceeds time limits."""
    pass

class ValidationError(AutomationError):
    """Raised when input validation fails."""
    pass

def raise_if_none(value, message):
    """Validate object existence."""
    if value is None:
        raise ValidationError(message)

def handle_retryable(func, attempts=3):
    """Decorator logic for function retries."""
    def wrapper(*args, **kwargs):
        last_ex = None
        for i in range(attempts):
            try:
                return func(*args, **kwargs)
            except AutomationError as e:
                last_ex = e
        raise last_ex
    return wrapper