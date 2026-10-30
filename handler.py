import logging
import time
from typing import Any, Callable, Dict, Optional

logger = logging.getLogger(__name__)


class TaskHandler:
    """Handles task execution with retry logic and edge case safety checks."""

    def __init__(self, max_retries: int = 3, backoff_factor: float = 0.5):
        self.max_retries = max(0, max_retries)
        self.backoff_factor = max(0.1, backoff_factor)

    def safe_execute(self, func: Callable[..., Any], payload: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Executes a callable safely, handling null payloads, bad types, and unexpected errors."""
        if payload is None:
            payload = {}
        elif not isinstance(payload, dict):
            logger.error(f"Invalid payload type: expected dict, got {type(payload).__name__}")
            return {"success": False, "error": "Invalid payload format", "result": None}

        attempts = 0
        last_error: Optional[Exception] = None

        while attempts <= self.max_retries:
            try:
                result = func(**payload)
                return {"success": True, "error": None, "result": result}
            except TypeError as err:
                # Catch signature or keyword parameter mismatches
                logger.warning(f"Parameter mismatch during execution of '{func.__name__}': {err}")
                return {"success": False, "error": f"Parameter error: {err}", "result": None}
            except Exception as err:
                attempts += 1
                last_error = err
                logger.error(f"Attempt {attempts} failed for '{func.__name__}': {err}")
                if attempts <= self.max_retries:
                    time.sleep(self.backoff_factor * (2 ** (attempts - 1)))

        return {
            "success": False,
            "error": f"Execution exhausted retries: {last_error}",
            "result": None,
        }
