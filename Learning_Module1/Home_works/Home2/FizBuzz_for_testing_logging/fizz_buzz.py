fizz = "Fizz"
buzz = "Buzz"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
result = []

import sys
import logging
import Learning_Module2.Home_works.Home10.homework.logger.my_logger as ext_logger

logger = ext_logger.external_logger_function_example()
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
    logger.info("after division we get: `" + str(division_result))
    return_result = division_result == 0
    logger.info("pure_division will return: `"+str(return_result))
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
    logging.info("analysis get: `"+str(element))
    if pure_division(element, 3) and pure_division(element, 5):
        return fizz + buzz
    elif pure_division(element, 3) and not pure_division(element, 5):
        return fizz
    elif not pure_division(element, 3) and pure_division(element, 5):
        return buzz
    else:
        return element


def get_result(numbers_list: list == numbers):
    '''
    Append to list result processing with analysis() for every element in numbers[]
    :return: list

    >>> get_result([1])
    [1]
    >>> get_result([3])
    [1, 'Fizz']
    >>> get_result([10])
    [1, 'Fizz', 'Buzz']

    '''

    for element in numbers_list:
        result.append(analysis(element))
    return result

# print("result: ", getResult())
# link to diagram https://drive.google.com/file/d/13Te0CYxa4-k5TP3SpTdmS0rL2lXsp2y8/view?usp=sharing
