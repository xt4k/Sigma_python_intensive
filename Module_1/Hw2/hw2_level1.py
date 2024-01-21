fizz = "Fizz"
buzz = "Buzz"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
result = []


def pure_division(base, element):
    return element % base == 0


def analysis(element):
    if (pure_division(3, element) and pure_division(5, element)):
        return fizz + buzz
    elif (pure_division(3, element) and not pure_division(5, element)):
        return fizz
    elif (not pure_division(3, element) and pure_division(5, element)):
        return buzz
    else:
        return element


def get_result():
    for element in numbers:
        result.append(analysis(element))
    return result


# print("result: ", getResult())
# link to diagram https://drive.google.com/file/d/13Te0CYxa4-k5TP3SpTdmS0rL2lXsp2y8/view?usp=sharing

