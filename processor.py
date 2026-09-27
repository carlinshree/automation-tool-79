import logging
from typing import Dict, Any, List, Optional

logger = logging.getLogger("automation_tool.processor")


class DataProcessor:
    """Processes a stream of automation tasks with strict input validation."""

    def __init__(self, required_keys: Optional[List[str]] = None) -> None:
        self.required_keys = required_keys or ["id", "action", "payload"]

    def validate_task(self, task: Any) -> bool:
        """Validates single task structure and field data types."""
        if not isinstance(task, dict):
            logger.warning("Invalid input type: expected a dictionary")
            return False

        # Verify presence of all required fields
        for key in self.required_keys:
            if key not in task:
                logger.warning(f"Validation failed: missing required key '{key}'")
                return False

        # Verify specific field types and constraints
        if not isinstance(task.get("id"), (int, str)):
            logger.warning("Validation failed: 'id' must be an integer or string")
            return False

        if not isinstance(task.get("action"), str) or not task["action"].strip():
            logger.warning("Validation failed: 'action' must be a non-empty string")
            return False

        if not isinstance(task.get("payload"), dict):
            logger.warning("Validation failed: 'payload' must be a dictionary")
            return False

        return True

    def process_batch(self, tasks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Executes the main processing loop with input validation checkpoints."""
        processed_results = []

        if not isinstance(tasks, list):
            logger.error("Invalid batch format: batch must be a list of tasks")
            return processed_results

        for index, raw_task in enumerate(tasks):
            logger.info(f"Evaluating task at batch index {index}")

            # Validate before executing any business logic
            if not self.validate_task(raw_task):
                logger.warning(f"Skipping invalid task at index {index}")
                continue

            # Extraction is safe after verification passes
            task_id = raw_task["id"]
            action = raw_task["action"].lower().strip()
            payload = raw_task["payload"]

            try:
                # Business logic processing
                result = {
                    "task_id": task_id,
                    "status": "success",
                    "executed_action": action,
                    "payload_size": len(payload)
                }
                processed_results.append(result)
            except Exception as exc:
                logger.error(f"Processing error on task {task_id}: {exc}")

        return processed_results
