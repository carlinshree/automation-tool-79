import logging
import sys
from typing import Optional

def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Configures and returns a standardized project logger."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

class AutomationLogger:
    """Wrapper for consistent application logging across modules."""
    def __init__(self, name: str = 'automation-tool-79'):
        self.logger = setup_logger(name)

    def info(self, msg: str) -> None:
        self.logger.info(msg)

    def error(self, msg: str, exc: Optional[Exception] = None) -> None:
        self.logger.error(msg, exc_info=exc)

    def warning(self, msg: str) -> None:
        self.logger.warning(msg)