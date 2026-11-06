import time
import functools
import logging
from typing import Callable, Any, Tuple, Type

logger = logging.getLogger(__name__)


def retry_network_operation(
    max_retries: int = 3,
    delay: float = 1.0,
    backoff_factor: float = 2.0,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,)
) -> Callable:
    """
    Decorator that retries a network operation with exponential backoff.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:
                    if attempt == max_retries:
                        logger.error(
                            "Operation '%s' failed after %d attempts: %s",
                            func.__name__, max_retries, exc
                        )
                        raise
                    logger.warning(
                        "Attempt %d/%d for '%s' failed: %s. Retrying in %.2fs...",
                        attempt, max_retries, func.__name__, exc, current_delay
                    )
                    time.sleep(current_delay)
                    current_delay *= backoff_factor
        return wrapper
    return decorator


def execute_with_retry(
    func: Callable,
    *args: Any,
    max_retries: int = 3,
    delay: float = 1.0,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
    **kwargs: Any
) -> Any:
    """Executes a given callable using retry backoff logic."""
    retry_decorator = retry_network_operation(
        max_retries=max_retries,
        delay=delay,
        exceptions=exceptions
    )
    return retry_decorator(func)(*args, **kwargs)
