import time
import random
import logging
from functools import wraps
from typing import Callable, Any, Tuple, Type

# Configure a logger for reporting retry events
logger = logging.getLogger("automation_tool.core")

def retry_operation(
    retries: int = 3,
    backoff_in_seconds: float = 1.0,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
) -> Callable:
    """
    Decorator that retries a function call using exponential backoff with jitter.
    
    :param retries: Maximum number of retry attempts allowed.
    :param backoff_in_seconds: Initial wait time in seconds.
    :param exceptions: Exception types that trigger a retry attempt.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempt = 0
            while attempt <= retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempt += 1
                    if attempt > retries:
                        logger.error(f"Failed '{func.__name__}' after {retries} retries. Final error: {e}")
                        raise e
                    
                    # Exponential backoff base with added jitter to avoid thundering herd problem
                    sleep_time = (backoff_in_seconds * (2 ** (attempt - 1))) + random.uniform(0.1, 0.5)
                    logger.warning(
                        f"Attempt {attempt}/{retries} failed for '{func.__name__}': {e}. "
                        f"Retrying in {sleep_time:.2f} seconds..."
                    )
                    time.sleep(sleep_time)
        return wrapper
    return decorator
