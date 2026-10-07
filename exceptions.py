class AutomationError(Exception):
    """Base exception for automation-tool-79."""
    pass

class DataValidationError(AutomationError):
    """Raised when input data fails schema or type checks."""
    pass

class ProcessingError(AutomationError):
    """Raised during internal transformation failures."""
    pass

class ConfigurationError(AutomationError):
    """Raised for missing or invalid environment variables."""
    pass

def handle_data_exception(e: Exception) -> dict:
    """Standardized structure for logging automation errors."""
    return {
        "error_type": e.__class__.__name__,
        "message": str(e),
        "status": "failed"
    }