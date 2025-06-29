import logging

def configure_logging():
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    if root_logger.hasHandlers():
        root_logger.handlers.clear()

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_format = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s')
    console_handler.setFormatter(console_format)

    error_handler = logging.FileHandler("error.log")
    error_handler.setLevel(logging.ERROR)
    error_format = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s')
    error_handler.setFormatter(error_format)

    root_logger.addHandler(console_handler)
    root_logger.addHandler(error_handler)
