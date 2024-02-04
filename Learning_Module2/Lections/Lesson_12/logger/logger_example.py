'''
Приклад реалізації логування
рівні:
logger.debug:       "Це буде видно лише розробникам
logger.info:        "Це виробничі дані, також збережені
logger.warning:     "Це використовується, коли чогось не вистачає, але програма все ще може працювати"
logger.error:       "Використовується всередині, крім блоків разом з об'єктами помилки, містить інформацію про помилку"
logger.critical     "Повідомляє, що програма завершила роботу і більше не може працювати, сигнал sys.exit(1)
'''

import os
import sys

'''
1. Ініціалізація імпорту модуля logging
'''
import logging


'''
2. Встановлення параметрів для конфігурування logging
'''
LOG_FILE_NAME = "log.txt"                                                               # ім'я файлу для запису інформації logging
DEFAULT_LOG_LEVEL = logging.DEBUG                                                       # рівень logging
DEFAULT_LOG_FORMAT = "%(levelname)s | %(filename)-15s: %(lineno)-4d | %(message)s"      # формат інформації logging
'''
Формат виводу повідомлення:
https://docs.python.org/3/library/logging.html
%(levelname)s                   - placeholder / псевдоелемен / місце відображення рівня logg
%(filename)-15s                 - placeholder ім'я файлу де реалізовано logg
%(lineno)-4d                    - placeholder рядок коду де реалізовано logg
%(message)s -                   - повідомлення logg, як аналог print
'''


''''
2.1. За потреби можна задати змінні середовищо:
Environment Variables  - змінні оточення / середовища. Ми вже використовували метод PATH із зверненням до os
Змінні середовища — це змінні, які встановлюються користувачем, операційною системою тощо поза програмою в її робочому середовищі.
Це пари ключ-значення, які використовуються операційними системами для зберігання інформації про середовище - шляхи та налаштування конфігурації.
Докладно - див. самостійно за посиланням
https://www.twilio.com/blog/how-to-set-environment-variables-html
https://blog.enterprisedna.co/python-set-environment-variable/
'''

LOG_LEVEL = os.environ.get("LOGLEVEL", DEFAULT_LOG_LEVEL)
# LOG_LEVEL = DEFAULT_LOG_LEVEL

'''
3. Конфігурування logg
filemode='a' - додавання інформації до файлу
filemode='w' - pfgbc інформації до файлу
'''
logging.basicConfig(filename=LOG_FILE_NAME, level=LOG_LEVEL, filemode='w', format=DEFAULT_LOG_FORMAT)

'''
4. Ініціалізація logg
'''
logger = logging.getLogger()


'''
4.1. Додавання консольного виводу інформації logg
'''
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(LOG_LEVEL)
console_handler.setFormatter(logging.Formatter(DEFAULT_LOG_FORMAT))
logger.addHandler(console_handler)

def logging_example_function() -> None:
    logger.debug("This will be visible only for developers %s %s", DEFAULT_LOG_LEVEL, DEFAULT_LOG_FORMAT)
    logger.info(f"This is production data, also saved to {LOG_FILE_NAME}")
    logger.warning("This is used, when something is missing, but program still can work")
    logger.error("Used inside except blocks together with error objects, contains information about the error")
    logger.critical("Notifies that the program ran into shutdown and couldn't work anymore sys.exit(1) signal. Worst case")
    
logging_example_function()




