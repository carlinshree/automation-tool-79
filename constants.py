import os
from typing import Final

# performance-critical thresholds
CACHE_EXPIRATION_SECONDS: Final[int] = 3600
MAX_WORKER_THREADS: Final[int] = os.cpu_count() or 4
CHUNK_SIZE_BYTES: Final[int] = 1024 * 1024 * 4

# memory optimization limits
MAX_MEMORY_BUFFER_MB: Final[int] = 512
STREAMING_THRESHOLD_BYTES: Final[int] = 10 * 1024 * 1024

# dictionary pre-allocation settings
INITIAL_MAP_CAPACITY: Final[int] = 1024
LOAD_FACTOR_THRESHOLD: Final[float] = 0.75

# connection pooling constants
DB_POOL_MIN_SIZE: Final[int] = 5
DB_POOL_MAX_SIZE: Final[int] = 20
CONNECTION_TIMEOUT: Final[float] = 30.0

def get_buffer_size() -> int:
    """Calculates optimized buffer based on platform constraints."""
    return CHUNK_SIZE_BYTES if MAX_MEMORY_BUFFER_MB > 256 else 1024 * 256