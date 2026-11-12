import logging
from logging.handlers import RotatingFileHandler
import os

# Application logging configuration
LOG_FILE = "automation-tool.log"
MAX_BYTES = 5 * 1024 * 1024  # 5MB
BACKUP_COUNT = 3

def setup_logger(name: str = "automation-tool") -> logging.Logger:
    """Initializes a rotating file logger for the application."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if re-initialized
    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # File rotation handler
        handler = RotatingFileHandler(
            LOG_FILE, 
            maxBytes=MAX_BYTES, 
            backup_count=BACKUP_COUNT
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # Optional: Console output for debugging
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)

    return logger

# Exported instance for quick access
logger = setup_logger()