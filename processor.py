import time
import random
import logging
from functools import wraps

logger = logging.getLogger(__name__)

def retry_network_operation(max_attempts=3, delay=2, backoff=2):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    if attempt == max_attempts:
                        logger.error(f"Final attempt failed: {e}")
                        raise
                    
                    sleep_time = current_delay + random.uniform(0, 1)
                    logger.warning(f"Attempt {attempt} failed, retrying in {sleep_time:.2f}s...")
                    time.sleep(sleep_time)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator

@retry_network_operation(max_attempts=3)
def fetch_data(url):
    """Mock function representing a volatile network request."""
    # Simulate network instability
    if random.random() < 0.7:
        raise ConnectionError("Server unreachable")
    return {"status": "success", "url": url}

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        result = fetch_data("https://api.example.com")
        print(f"Result: {result}")
    except Exception as e:
        print(f"Operation failed after retries: {e}")