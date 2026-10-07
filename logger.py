import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name='automation-tool-79', log_file='app.log', level=logging.INFO):
    """
    Configures a rotating file logger for system tracking.
    Max file size: 5MB, keep 3 backup files.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if function is called multiple times
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Rotating file handler configuration
        file_handler = RotatingFileHandler(
            log_file, 
            maxBytes=5 * 1024 * 1024, 
            backupCount=3
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Optional stream handler for console output
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    return logger

# Instance for global application usage
logger = setup_logger()