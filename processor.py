import time
import random
import logging
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger("automation_tool.processor")

def retry_on_failure(
    retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,)
) -> Callable:
    """
    Decorator that retries a function call with exponential backoff.
    
    :param retries: Maximum number of retry attempts.
    :param delay: Initial delay between retries in seconds.
    :param backoff: Multiplier applied to the delay after each retry.
    :param exceptions: Tuple of exceptions that trigger a retry.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for attempt in range(retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == retries:
                        logger.error(
                            "Execution failed after %d attempts. Error: %s",
                            retries + 1,
                            e
                        )
                        raise e
                    
                    # Apply small jitter to prevent thundering herd problem
                    jitter = random.uniform(0, 0.1 * current_delay)
                    sleep_time = current_delay + jitter
                    
                    logger.warning(
                        "Attempt %d failed: %s. Retrying in %.2f seconds...",
                        attempt + 1,
                        e,
                        sleep_time
                    )
                    time.sleep(sleep_time)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator

@retry_on_failure(retries=3, delay=1.5, exceptions=(ConnectionError, TimeoutError))
def execute_network_request(url: str) -> str:
    """Simulates a network request that might temporarily fail."""
    # 70% chance to simulate a network glitch for demonstration purposes
    if random.random() < 0.7:
        raise ConnectionError("Temporary connection failure")
    return f"Success: response from {url}"
