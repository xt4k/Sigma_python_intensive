
'''
Функціональне програмування
'''


#------------------------- опис функцій ---------------------------------

def area_triangle_1():
    text = 'Площа трикутника'  # Увага hardcode - функція залежить від фіксованих аргументів
    a = 10.0
    h = 22.0
    s = (1 / 2) * a * h
    output_s = dict(result=text, triangle_parameter_a=a, triangle_parameter_h=h, out=s)
    print(output_s, '\n')
    return


def area_triangle_2(a, h, text):
    s = (1 / 2) * a * h
    output_s = dict(result=text, triangle_parameter_a=a, triangle_parameter_h=h, out=s)
                                # Увага порушення PEP - параметри, що подаються на вхід - потрапляють на "вихід", п.1,2,3.
    return output_s


def area_triangle_3(a, h):
    return (1 / 2) * a * h

#------------------------- виклик функцій ---------------------------------

'''
Конструкція з явно визначеною точкою старту програми - по факту - декларація основного блоку програми
https://www.freecodecamp.org/ukrainian/news/poyasnennya-if-name-main-u-python-z-prykladamy/
https://medium.com/@mycodingmantras/what-does-if-name-main-mean-in-python-fa6b0460a62d

'''

# print("Точка старту???", area_triangle_1())


if __name__ == "__main__":

    area_triangle_1()

    print(area_triangle_2(10.0, 22.0, 'Площа трикутника'), '\n')

    text = 'Площа трикутника'
    a = 10.0
    h = 22.0
    test_1 = area_triangle_3(a, h)
    print(text, ' ', test_1, '\n')


