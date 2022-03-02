import logging
import os

from app.config import APP_LOG_FILE_NAME


def set_logging_parameters(logger: logging.Logger) -> logging.Logger:
    logger.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(os.path.join(os.getcwd(), "logs", APP_LOG_FILE_NAME))
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(levelname)s:     %(name)s - %(asctime)s - %(message)s")
    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    return logger
