import time
import logging
import functools
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger("automation_tool")


class NetworkError(Exception):
    """Raised when network operation fails after maximum retries."""
    pass


def retry_on_failure(
    retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,)
) -> Callable:
    """Decorator that retries network operations using exponential backoff."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    if attempt == retries:
                        logger.error("Failed %s after %d retries: %s", func.__name__, retries, err)
                        raise NetworkError(f"Operation failed after {retries} retries") from err

                    logger.warning(
                        "Attempt %d/%d for %s failed with error: %s. Retrying in %.1fs...",
                        attempt, retries, func.__name__, err, current_delay
                    )
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator


class NetworkHandler:
    """Manages network requests with configurable retry logic."""

    def __init__(self, max_retries: int = 3, initial_delay: float = 1.0):
        self.max_retries = max_retries
        self.initial_delay = initial_delay

    def execute_request(self, func: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
        """Executes a target network function wrapped with retry handling."""
        decorated_func = retry_on_failure(
            retries=self.max_retries,
            delay=self.initial_delay
        )(func)
        return decorated_func(*args, **kwargs)
