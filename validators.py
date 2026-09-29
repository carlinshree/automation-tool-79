import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry_operation(max_retries: int = 3, delay: float = 1.0):
    """
    Decorator for retrying network operations on failure.
    """
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}")
                    if attempt < max_retries - 1:
                        time.sleep(delay * (2 ** attempt))
            logger.error(f"Operation failed after {max_retries} attempts")
            raise last_exception
        return wrapper
    return decorator

@retry_operation(max_retries=3, delay=2.0)
def fetch_network_resource(url: str) -> str:
    """
    Example network call wrapper.
    """
    # Simulating actual network logic
    import random
    if random.random() < 0.7:
        raise ConnectionError("Network unstable")
    return f"Data from {url}"