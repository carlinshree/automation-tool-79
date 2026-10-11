import logging
import os

# Configuration constants for automation-tool-79
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3
LOG_LEVEL = logging.INFO

# Path constants with existence validation
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.getenv('DATA_PATH', os.path.join(BASE_DIR, 'data'))

# Error message constants for consistent logging
ERR_MSG_CONNECTION = "Connection failed: network unreachable"
ERR_MSG_TIMEOUT = "Operation exceeded the specified timeout duration"
ERR_MSG_PERMISSION = "Access denied: insufficient file system permissions"
ERR_MSG_INVALID_INPUT = "Validation error: unexpected input data format"

# Supported environment mapping
ENV_MODES = {
    'dev': 'development_config.json',
    'prod': 'production_config.json',
    'test': 'testing_config.json'
}

def validate_path_availability(path: str) -> bool:
    """Checks if a directory is accessible for automation tasks."""
    try:
        return os.path.exists(path) and os.access(path, os.R_OK | os.W_OK)
    except OSError:
        return False

# Setup logger to match application requirements
logger = logging.getLogger('automation-tool-79')
if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(LOG_LEVEL)