import logging
from logging.handlers import RotatingFileHandler

def setup_logger(name, log_file, level=logging.INFO):
    # Create a logger object
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create a rotating file handler which rotates log files
    handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=3)
    handler.setLevel(level)

    # Create a formatter and set it for the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    return logger

if __name__ == '__main__':
    # Example usage
    logger = setup_logger('my_logger', 'app.log')
    logger.info('Logger is set up and ready to use!')