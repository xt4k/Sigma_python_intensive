
'''

Приклад тестування файл-менеджера з функціоналом:
- логування - logging;
- контроль виключень - try: except;
Тестуванню підлягають процеси, а не результати обчислень:
- створення файлу,
- читання файлу з урахуванням виключення

Особливість: logging - не створено, та не надано!!!

'''


from logging import Logger


class FileSettings:
    def __init__(self, file_name: str, file_extension: str, mode: str, suffix: str = ""):
        self.file_name = file_name
        self.file_extension = file_extension
        self.mode = mode
        self.suffix = suffix

    def get_file_name(self):
        return f"{self.file_name}{'-' + self.suffix if self.suffix else ''}.{self.file_extension}"


class FileManager:

    def __init__(self, logger: Logger):
        self.logger = logger                    # Особливість: logging - не створено, та не надано!!!

    def get_file(self, file_settings: FileSettings):
        try:
            with open(mode=file_settings.mode, file=file_settings.get_file_name()) as file:
                return file.name
        except Exception as ex:
            self.logger.error(ex)
            raise
