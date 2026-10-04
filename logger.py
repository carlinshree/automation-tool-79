import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name='automation-tool', log_file='app.log', level=logging.INFO):
    """Configures a rotating file logger for automation-tool-79."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if setup is called multiple times
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Rotate files: max 5MB, keep 3 backup files
        file_handler = RotatingFileHandler(
            log_file, 
            maxBytes=5 * 1024 * 1024, 
            backupCount=3
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Add console output for development visibility
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

if __name__ == '__main__':
    # Example usage for verification
    log = setup_logger()
    log.info('logger initialization successful')