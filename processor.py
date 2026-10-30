import logging

logger = logging.getLogger(__name__)

def process_data(data: list) -> list:
    """Processes input list with validation and error handling."""
    if not isinstance(data, list):
        logger.error(f"Invalid input type: {type(data)}")
        return []

    processed = []
    for index, item in enumerate(data):
        try:
            if item is None:
                raise ValueError("null value encountered")
            processed.append(float(item) * 2)
        except (ValueError, TypeError) as e:
            logger.warning(f"Skipping item at index {index}: {e}")
            continue
    
    return processed

def batch_transform(data_sequence: list) -> dict:
    """Transforms sequences with robust error recovery."""
    results = {"success": [], "errors": 0}
    
    for entry in data_sequence:
        try:
            transformed = process_data(entry)
            results["success"].extend(transformed)
        except Exception as e:
            logger.critical(f"Unexpected system failure: {e}")
            results["errors"] += 1
            
    return results