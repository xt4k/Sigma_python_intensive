'''
Об'єкт тестування з модулем unittest

'''

def add(a, b) -> int:
    return a + b


def division(a, b) -> int:
    try:
        return a // b
    except ZeroDivisionError:
        raise
