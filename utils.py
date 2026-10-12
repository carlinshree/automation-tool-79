import logging
import random
import time
import urllib.error
import urllib.request
from typing import Any, Callable, Tuple, Type

logger = logging.getLogger(__name__)

def retry_network_op(
    max_retries: int = 3,
    backoff_factor: float = 1.0,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,)
) -> Callable:
    """
    Decorator that retries a function upon catching specified exceptions,
    using exponential backoff with random jitter.
    """
    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            retries = 0
            while True:
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:
                    retries += 1
                    if retries > max_retries:
                        logger.error("Max retries (%d) reached for %s: %s", max_retries, func.__name__, exc)
                        raise exc
                    
                    sleep_time = (backoff_factor * (2 ** (retries - 1))) + random.uniform(0, 0.5)
                    logger.warning(
                        "Attempt %d/%d failed for %s (%s). Retrying in %.2fs...",
                        retries, max_retries, func.__name__, exc, sleep_time
                    )
                    time.sleep(sleep_time)
        return wrapper
    return decorator

def fetch_url_with_retry(url: str, timeout: int = 10) -> str:
    """Example network call wrapper using urllib with automatic retries."""
    @retry_network_op(max_retries=3, backoff_factor=0.5, exceptions=(urllib.error.URLError, TimeoutError))
    def _fetch():
        req = urllib.request.Request(url, headers={"User-Agent": "AutomationTool/1.0"})
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return response.read().decode("utf-8")

    return _fetch()
