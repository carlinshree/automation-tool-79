import logging
import sys
from pathlib import Path

def setup_logger(name: str, log_file: str = 'app.log', level: int = logging.INFO) -> logging.Logger:
    """Configures a standard logger for automation tasks."""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # File handler
    log_path = Path(log_file)
    file_handler = logging.FileHandler(log_path)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger

def get_module_logger(module_name: str) -> logging.Logger:
    """Factory function for consistent module-level logging."""
    return setup_logger(module_name)