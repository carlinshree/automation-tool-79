import logging

logger = logging.getLogger(__name__)

def process_data(data: list) -> list:
    """Process raw data list with boundary and type validation."""
    if not isinstance(data, list):
        logger.error("Invalid input type: expected list")
        return []

    processed = []
    for item in data:
        try:
            # Ensure numeric operations don't fail on mixed types
            if not isinstance(item, (int, float)):
                logger.warning(f"Skipping non-numeric entry: {item}")
                continue
            
            # Simulate processing logic
            result = float(item) * 1.05
            processed.append(round(result, 2))
            
        except (ValueError, TypeError) as e:
            logger.error(f"Data transformation error on {item}: {e}")
            continue
        except Exception as e:
            logger.critical(f"Unexpected system fault: {e}")
            raise

    return processed

def validate_batch(batch: dict) -> bool:
    """Verify dictionary structure before pipeline ingestion."""
    required_keys = {'id', 'payload'}
    try:
        if not isinstance(batch, dict):
            return False
        return required_keys.issubset(batch.keys())
    except AttributeError:
        return False