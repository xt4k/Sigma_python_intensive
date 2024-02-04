'''
Приклад реалізації логування з налаштуваннями із файлу
'''

import logging
import logging.config

#  Конфігурування logg
# logging.config.fileConfig('temp.conf')
logging.config.fileConfig('config.txt')

# Ініціалізація logg
logger = logging.getLogger('simpleExample')

# Тестові повідомлення
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')