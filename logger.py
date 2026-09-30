import logging
import functools
import time
from typing import Callable, Any

# Configure structured logging for automation-tool-79
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('core_logger')

# Cache for function performance optimization
_performance_cache = {}

def profile_execution(func: Callable) -> Callable:
    """Decorator for tracking function execution duration."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start_time
        
        # Log slow executions exceeding 100ms
        if duration > 0.1:
            logger.warning(f'slow execution in {func.__name__}: {duration:.4f}s')
        return result
    return wrapper

def get_cached_config(key: str, default: Any = None) -> Any:
    """Memory-efficient config lookup using internal cache."""
    if key not in _performance_cache:
        # Simulate IO-bound config fetch
        _performance_cache[key] = default
    return _performance_cache[key]

class PerformanceHandler:
    """Context manager for resource cleanup and profiling."""
    def __init__(self, name: str):
        self.name = name

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.perf_counter() - self.start
        logger.info(f'operation {self.name} completed in {elapsed:.4f}s')