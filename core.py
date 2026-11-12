import logging

def validate_input(data):
    """Ensures data is a non-empty dictionary."""
    if not isinstance(data, dict) or not data:
        raise ValueError("Invalid payload: expected non-empty dictionary")
    if 'id' not in data:
        raise KeyError("Invalid payload: missing required key 'id'")
    return True

def run_processing_loop(queue):
    """Main orchestration loop for automation-tool-79."""
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    while True:
        task = queue.get()
        if task is None:
            break
            
        try:
            # Validate payload before processing
            validate_input(task)
            
            # Execute core business logic
            result = task.get("id") * 2
            logger.info(f"Processed task {task.get('id')}: result {result}")
            
        except (ValueError, KeyError) as e:
            logger.error(f"Skipping invalid task: {e}")
        except Exception as e:
            logger.critical(f"Unexpected error: {e}")
            continue

if __name__ == "__main__":
    from queue import Queue
    test_queue = Queue()
    test_queue.put({"id": 10})
    test_queue.put("bad_data")
    test_queue.put(None)
    run_processing_loop(test_queue)