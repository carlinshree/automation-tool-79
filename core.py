import logging
from typing import Any, Dict, List

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def validate_task_payload(data: Dict[str, Any]) -> bool:
    """Validate task dictionary structure and types before processing."""
    if not isinstance(data, dict):
        logging.warning("Invalid input: payload is not a dictionary.")
        return False

    required_keys = {"task_id", "action", "params"}
    if not required_keys.issubset(data.keys()):
        missing = required_keys - set(data.keys())
        logging.warning(f"Invalid input: missing required keys: {missing}")
        return False

    if not isinstance(data["task_id"], (int, str)) or not str(data["task_id"]).strip():
        logging.warning("Invalid input: task_id must be a non-empty string or integer.")
        return False

    if not isinstance(data["params"], dict):
        logging.warning("Invalid input: params must be a dictionary.")
        return False

    return True


def execute_task(task: Dict[str, Any]) -> bool:
    """Simulate execution of a validated automation task."""
    logging.info(f"Executing task '{task['task_id']}' with action '{task['action']}'")
    return True


def run_processing_loop(batch_data: List[Dict[str, Any]]) -> Dict[str, int]:
    """Process a batch of automation tasks with strict input validation."""
    stats = {"processed": 0, "skipped": 0, "failed": 0}

    for item in batch_data:
        # Input validation guard
        if not validate_task_payload(item):
            stats["skipped"] += 1
            continue

        try:
            success = execute_task(item)
            if success:
                stats["processed"] += 1
            else:
                stats["failed"] += 1
        except Exception as err:
            logging.error(f"Error processing task {item.get('task_id')}: {err}")
            stats["failed"] += 1

    return stats


if __name__ == "__main__":
    sample_tasks = [
        {"task_id": "T-101", "action": "backup", "params": {"target": "/data"}},
        {"task_id": "", "action": "cleanup", "params": {}},
        "invalid_item",
        {"task_id": 102, "action": "sync", "params": {"retries": 3}},
    ]
    results = run_processing_loop(sample_tasks)
    logging.info(f"Batch processing completed: {results}")
