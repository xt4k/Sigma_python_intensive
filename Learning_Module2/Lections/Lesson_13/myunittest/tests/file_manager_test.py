
'''

Приклад тестування файл-менеджера з функціоналом:
- логування - logging;
- контроль виключень - try: except;
Тестуванню підлягають процеси, а не результати обчислень:
- створення файлу,
- читання файлу з урахуванням виключення

Особливість: logging - не створено, та не надано!!!
logging замінює динамічний обєкт Mock()

'''

import unittest
from unittest.mock import Mock

from ..myfile.file_manager import FileSettings, FileManager


class FileManagerTests(unittest.TestCase):

    def test_file_manager_creates_file_with_name(self):
        settings = FileSettings("test", "txt", "w", "test")
        logger_mock = Mock()                                        # logging замінює динамічний обєкт Mock()
        manager = FileManager(logger=logger_mock)

        file_name = manager.get_file(settings)

        self.assertTrue("test-test.txt" in file_name)               # тест-контроль відповідності імя файлу заданому формату

    def test_file_manager_logger_error_is_called(self):
        settings = FileSettings("test2", "txt", "r", "test")
        logger_mock = Mock()
        manager = FileManager(logger=logger_mock)
                                                                    # тут можуть бути умови, що призводять до виключення
        self.assertRaises(Exception, manager.get_file, settings)    # тест-контроль опрацювання виключення

if __name__ == '__main__':
    unittest.main()