import concurrent.futures
from typing import List, Dict, Any, Callable

class CoreEngine:
    '''
    Core execution engine optimized for parallel task processing and
    redundant task deduplication using memory-based caching.
    '''
    def __init__(self, max_workers: int = 4):
        self.max_workers = max_workers
        self._cache: Dict[str, Any] = {}

    def _get_cache_key(self, task_name: str, args: tuple, kwargs: dict) -> str:
        # Generate a unique cache key based on task identity and arguments
        str_kwargs = sorted([(k, str(v)) for k, v in kwargs.items()])
        return f'{task_name}:{hash(args)}:{hash(tuple(str_kwargs))}'

    def run_task(self, task_id: str, func: Callable, *args, **kwargs) -> Any:
        # Execute single task with caching mechanism
        cache_key = self._get_cache_key(task_id, args, kwargs)
        if cache_key in self._cache:
            return self._cache[cache_key]

        result = func(*args, **kwargs)
        self._cache[cache_key] = result
        return result

    def execute_batch(self, tasks: List[Dict[str, Any]]) -> List[Any]:
        '''
        Executes a list of tasks in parallel using a ThreadPoolExecutor.
        Each task dict contains: 'id', 'func', and optional 'args' and 'kwargs'.
        '''
        results = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {}
            for task in tasks:
                task_id = task['id']
                func = task['func']
                args = task.get('args', ())
                kwargs = task.get('kwargs', {})

                cache_key = self._get_cache_key(task_id, args, kwargs)
                if cache_key in self._cache:
                    results.append(self._cache[cache_key])
                    continue

                future = executor.submit(func, *args, **kwargs)
                futures[future] = (task_id, args, kwargs)

            for future in concurrent.futures.as_completed(futures):
                task_id, args, kwargs = futures[future]
                try:
                    result = future.result()
                    cache_key = self._get_cache_key(task_id, args, kwargs)
                    self._cache[cache_key] = result
                    results.append(result)
                except Exception as e:
                    results.append(e)

        return results