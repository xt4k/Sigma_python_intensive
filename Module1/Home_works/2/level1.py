fizz = "Fizz"
buzz = "Buzz"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
result = []


def pure_division(element: int, base: int) -> bool:
    '''
     return true if parameter `element` is divided to `base` without rest.
    in other case return false
    :param element: number that will be divided to `base`
    :param base: number to which we divide `element`
    :return: true/false
    '''

    return element % base == 0


def analysis(element: int):
    '''
    check if parameter element is can be divided without rest to 3 and/or  5
    and according to it - return or element or String
    :param element:  - number that checked
    :return: integer or string
    '''
    if pure_division(element, 3) and pure_division(element, 5):
        return fizz + buzz
    elif pure_division(element, 3) and not pure_division(element, 5):
        return fizz
    elif not pure_division(element, 3) and pure_division(element, 5):
        return buzz
    else:
        return element


def get_result():
    '''
    Append to list result processing with analysis() for every element in numbers[]
    :return: list
    '''

    for element in numbers:
        result.append(analysis(element))
    return result

# print("result: ", getResult())
# link to diagram https://drive.google.com/file/d/13Te0CYxa4-k5TP3SpTdmS0rL2lXsp2y8/view?usp=sharing
