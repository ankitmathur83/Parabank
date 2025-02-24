import logging

def setup_logger():
    # Create a logger
    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.INFO)

    # Create a log format
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    formatter = logging.Formatter(log_format)

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Create a file handler to log to a file (optional)
    file_handler = logging.FileHandler('test_execution.log')
    file_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

