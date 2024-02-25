'''
This is an examples for logging function that may be used as external info module
'''

import sys
import logging


def external_logger_function_example(file_name="my_pytest.log"):
    LOG_FILE_NAME = file_name
    DEFAULT_LOG_LEVEL = logging.INFO
    DEFAULT_LOG_FORMAT = "%(asctime)s %(levelname)s | %(filename)-15s: %(lineno)-4d | %(message)s"
    logging.basicConfig(filename=LOG_FILE_NAME, level=DEFAULT_LOG_LEVEL, filemode='w', format=DEFAULT_LOG_FORMAT)

    logger = logging.getLogger()

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(DEFAULT_LOG_LEVEL)
    console_handler.setFormatter(logging.Formatter(DEFAULT_LOG_FORMAT))

    logger.addHandler(console_handler)

    return logger
