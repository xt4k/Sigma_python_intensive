import string

fizz = "Fizz"
buzz = "Buzz"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
result = []

import logging
from Learning_Module2.Home_works.Home10.homework.logger.my_logger import external_logger_function_example as ext_logger

logger = ext_logger("log-test.log")


def pure_division(element: int, base: int) -> bool:
    '''
     return true if parameter `element` is divided to `base` without rest.
    in other case return false
    :param element: number that will be divided to `base`
    :param base: number to which we divide `element`
    :return: true/false

    >>> pure_division(13, 2)
    False
    >>> pure_division(12, 4)
    True
    >>> pure_division(0, 4)
    True

    '''

    division_result = element % base
    return_result = division_result == 0
    logging.debug("pure_division: `{}`,`{}`->`{}`".format(element, base, return_result))
    return return_result


def analysis(element: int):
    '''
    check if parameter element is can be divided without rest to 3 and/or  5
    and according to it - return or element or String
    :param element:  - number that checked
    :return: integer or string

    >>> analysis(6)
    'Fizz'
    >>> analysis(10)
    'Buzz'
    >>> analysis(15)
    'FizzBuzz'
    >>> analysis(8)
    8

    '''
    returned = None

    if pure_division(element, 3) and pure_division(element, 5):
        returned = fizz + buzz
    elif pure_division(element, 3) and not pure_division(element, 5):
        returned = fizz
    elif not pure_division(element, 3) and pure_division(element, 5):
        returned = buzz
    else:
        returned = element
    logging.info("analysis: `{}`->`{}`".format(element, returned))
    return returned


def get_result(numbers_list: list == numbers):
    """
    Append to list result processing with analysis() for every element in numbers[]
    :return: list
    >>> get_result([1])
    [1]
    >>> get_result([3])
    [1, 'Fizz']
    >>> get_result([10])
    [1, 'Fizz', 'Buzz']

    """
    for element in numbers_list:
        result.append(analysis(element))
    logging.info("get_result: `{}`".format(result))
    return result