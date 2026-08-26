import time
import logging
from functools import wraps
from requests.exceptions import RequestException

logger = logging.getLogger('automation-tool-79')

def retry_operation(retries=3, delay=2, backoff=2):
    """Decorator to retry network operations with exponential backoff."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            attempt = 0
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except RequestException as e:
                    attempt += 1
                    if attempt == retries:
                        logger.error(f"Operation failed after {retries} attempts: {e}")
                        raise
                    logger.warning(f"Attempt {attempt} failed: {e}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

@retry_operation(retries=3, delay=1)
def fetch_data_from_endpoint(url):
    """Example network operation function."""
    import requests
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.json()
