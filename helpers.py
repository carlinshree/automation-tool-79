import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_network_operation(max_attempts=3, delay=2, exceptions=(Exception,)): 
    """Decorator for retrying functions on transient failures."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt} failed for {func.__name__}: {e}")
                    if attempt < max_attempts:
                        time.sleep(delay)
            
            logger.error(f"Operation {func.__name__} failed after {max_attempts} attempts")
            raise last_exception
        return wrapper
    return decorator