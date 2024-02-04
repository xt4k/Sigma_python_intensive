
'''
Приклади:

* документування коду - docstring;
    використовується для повторного використання коду / створення документації на проект.
* використання тестів в документації -  doctest;
    використовується для первинного тестування коду / "тестування" оновлення документації.

'''


import doctest


def add(a: int, b: int) -> int:

    '''
    Returns a sum of two numbers
    :param a: first number for sum
    :param b: second number for sum
    :return: sum of 'a' and 'b'

    >>> add(1, 2)
    3
    >>> add(0, 2)
    2

    '''

    # """
    # Returns a sum of two numbers
    # :param a: first number for sum
    # :param b: second number for sum
    # :return: sum of 'a' and 'b'
    #
    # >>> add(1, 2)
    # 3
    # >>> add(0, 2)
    # 2
    #
    # """


    return a + b


def division(a: int, b: int) -> int:
    """
    divides 'a' by 'b'
    :param a: divident
    :param b: divider
    :return: division of 'a' by 'b'
    >>> division(1, 1)
    1
    >>> division(1, 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: integer division or modulo by zero
    """
    return a // b


if __name__ == '__main__':
    doctest.testmod(verbose=True)
