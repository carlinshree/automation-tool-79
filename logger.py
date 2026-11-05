import os
import sys
import logging
from logging.handlers import RotatingFileHandler
from typing import Optional

DEFAULT_LOG_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s:%(funcName)s:%(lineno)d - %(message)s"
DEFAULT_LOG_DIR = "logs"
DEFAULT_LOG_FILE = "automation.log"


def setup_logger(
    name: str = "automation_tool",
    log_level: int = logging.INFO,
    log_dir: str = DEFAULT_LOG_DIR,
    log_file: str = DEFAULT_LOG_FILE,
    max_bytes: int = 5 * 1024 * 1024,
    backup_count: int = 5,
    log_format: Optional[str] = None,
) -> logging.Logger:
    """Configures and returns a logger with console and rotating file output handlers."""
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    if logger.hasHandlers():
        logger.handlers.clear()

    formatter = logging.Formatter(log_format or DEFAULT_LOG_FORMAT)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    os.makedirs(log_dir, exist_ok=True)
    file_path = os.path.join(log_dir, log_file)

    file_handler = RotatingFileHandler(
        file_path,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


def get_logger(name: str = "automation_tool") -> logging.Logger:
    """Retrieves an existing logger or initializes a default logger."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        return setup_logger(name=name)
    return logger
