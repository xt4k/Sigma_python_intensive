'''
Приклад логування генератора-функції (генераторна функція)
'''


import sys
import logging


def my_generator(start, end, step=1):
    current = start
    while current <= end:
        yield current
        yield current ** 2
        current += step


def logging_example_function():

    LOG_FILE_NAME = "my_pytest.log"

    # DEFAULT_LOG_LEVEL = logging.INFO      # Демонстрацція рівня повідомлень

    DEFAULT_LOG_LEVEL = logging.DEBUG       # Демонстрацція рівня повідомлень

    DEFAULT_LOG_FORMAT = "%(asctime)s %(levelname)s | %(filename)-15s: %(lineno)-4d | %(message)s"
    logging.basicConfig(filename=LOG_FILE_NAME, level=DEFAULT_LOG_LEVEL, filemode='w', format=DEFAULT_LOG_FORMAT)

    logger = logging.getLogger()

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(DEFAULT_LOG_LEVEL)
    console_handler.setFormatter(logging.Formatter(DEFAULT_LOG_FORMAT))

    logger.addHandler(console_handler)

    return logger


my_gen = my_generator(1, 10)
logger = logging_example_function()


if __name__ == '__main__':

    for x in my_gen:
        logger.debug(x)
        # print(x)