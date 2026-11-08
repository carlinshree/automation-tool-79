import time
import functools
import requests
from typing import Callable, Any

def with_retry(max_attempts: int = 3, delay: float = 1.0):
    """Decorator to retry network operations on request failures."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except requests.exceptions.RequestException as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        time.sleep(delay * (2 ** attempt))
                        continue
            raise last_exception
        return wrapper
    return decorator

@with_retry(max_attempts=3, delay=2.0)
def fetch_url(url: str) -> str:
    """Fetches content from a URL with built-in retry logic."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text