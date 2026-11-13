import time
import random
import functools
from typing import Callable, Any

def retry_with_backoff(retries: int = 3, backoff_in_seconds: float = 1.0):
    """
    Decorator to retry network operations with exponential backoff.
    """
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            x = 0
            while True:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if x == retries:
                        raise e
                    
                    sleep = (backoff_in_seconds * 2 ** x) + random.uniform(0, 1)
                    time.sleep(sleep)
                    x += 1
        return wrapper
    return decorator

@retry_with_backoff(retries=3, backoff_in_seconds=2.0)
def network_request_mock(url: str):
    """
    Example function demonstrating retry logic for connectivity.
    """
    print(f"Attempting request to {url}")
    # Simulate transient network failure
    if random.random() < 0.7:
        raise ConnectionError("Transient network error occurred")
    return "Success"