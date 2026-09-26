import logging
import os
import sys

def setup_logger(name: str, log_file: str = 'app.log') -> logging.Logger:
    """Configures a robust logger with file system edge case handling."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    try:
        # Ensure log directory exists
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)

        # Create file handler with basic permission error protection
        handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    except (PermissionError, OSError) as e:
        # Fallback to stderr if file logging fails
        fallback = logging.StreamHandler(sys.stderr)
        logger.addHandler(fallback)
        logger.error(f"failed to initialize file logger: {e}. fallback to stderr active.")

    return logger