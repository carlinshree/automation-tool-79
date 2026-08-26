import time
from functools import lru_cache
from typing import Any, Callable

class PerformanceOptimizer:
    def __init__(self, cache_size: int = 128) -> None:
        self.cache_size = cache_size

    def memoize_operation(self, func: Callable[..., Any]) -> Callable[..., Any]:
        """Caches function results to improve execution speed."""
        cached_func = lru_cache(maxsize=self.cache_size)(func)
        return cached_func

    def benchmark(self, func: Callable[..., Any], *args: Any, **kwargs: Any) -> tuple[Any, float]:
        """Measures execution time of a target function."""
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        return result, execution_time

@lru_cache(maxsize=256)
def compute_heavy_task(data_factor: int) -> int:
    """Simulates a computationally expensive core process."""
    total = 0
    for i in range(data_factor * 1000):
        total += i * i
    return total

def execute_optimized_workflow(factor: int) -> int:
    optimizer = PerformanceOptimizer()
    optimized_task = optimizer.memoize_operation(compute_heavy_task)
    
    _, duration = optimizer.benchmark(optimized_task, factor)
    print(f"Execution completed in {duration:.6f} seconds")
    
    return optimized_task(factor)
