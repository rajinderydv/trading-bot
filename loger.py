import os
import logging
from logging.handlers import RotatingFileHandler
import config


def setup_logger():

    # Create logs folder if it doesn't exist
    if not os.path.exists(config.LOG_FOLDER):
        os.makedirs(config.LOG_FOLDER)

    log_file = os.path.join(config.LOG_FOLDER, "trading_bot.log")

    logger = logging.getLogger("TradingBot")

    # Prevent duplicate handlers
    if logger.hasHandlers():
        return logger

    logger.setLevel(getattr(logging, config.LOG_LEVEL.upper()))

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    # File logger
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=5 * 1024 * 1024,
        backupCount=5
    )
    file_handler.setFormatter(formatter)

    # Console logger
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


logger = setup_logger()