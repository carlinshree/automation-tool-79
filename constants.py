import functools
from typing import Final

# Performance constants for automation-tool-79

CACHE_SIZE_LIMIT: Final[int] = 1024
TIMEOUT_SECONDS: Final[int] = 30
BATCH_CHUNK_SIZE: Final[int] = 500

@functools.lru_cache(maxsize=CACHE_SIZE_LIMIT)
def get_optimized_multiplier(factor: float) -> float:
    """Calculates factor-based thresholds with memoization."""
    return factor * 1.5

class ProcessingDefaults:
    """Centralized configurations for core performance tuning."""
    BUFFER_SIZE = 65536
    THREAD_POOL_WORKERS = 4
    MAX_RETRIES = 3

# Default operation timeouts
TASK_TIMEOUTS = {
    'network': 60,
    'disk': 10,
    'cpu': 30
}

# Data alignment constants for memory optimization
BYTE_ALIGNMENT: Final[int] = 8