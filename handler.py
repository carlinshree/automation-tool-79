import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_operation(retries=3, delay=2, exceptions=(ConnectionError, TimeoutError)):
    """Decorator to retry network operations on failure."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
            
            logger.error(f"All {retries} retries exhausted.")
            raise last_exception
        return wrapper
    return decorator

@retry_operation(retries=3, delay=1)
def fetch_data(url):
    """Simulated network request with potential for failure."""
    logger.info(f"Requesting data from {url}")
    # Simulate network instability logic here
    return {"status": "success", "url": url}