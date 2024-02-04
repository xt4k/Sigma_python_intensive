'''
Короткий приклад реалізації логування
'''

import logging

#  Конфігурування logg
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

# Ініціалізація logg
logger = logging.getLogger()

# Встановлення порогового значення реєстратора на DEBUG
logger.setLevel(logging.DEBUG)

# Тестові повідомлення
logger.debug("Harmless debug Message")
logger.info("Just an information")
logger.warning("Its a Warning")
logger.error("Did you try to divide by zero")
logger.critical("Internet is down")