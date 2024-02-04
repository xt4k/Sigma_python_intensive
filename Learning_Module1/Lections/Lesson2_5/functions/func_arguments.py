
'''
Способи передачі параметрів до функції - аргументи через інтерфейс (специфікацію)
'''


#------------------------- опис функцій ---------------------------------

def area_triangle_1(a, h, text):
    s = (1 / 2) * a * h
    output_s = dict(result=text, triangle_parameter_a=a, triangle_parameter_h=h, out=s)
    print(output_s)
    return output_s


def area_triangle_2(a, h):
    return ((1 / 2) * a * h)


def area_triangle_3(a, h):
    s = (1 / 2) * a * h
    return s

def area_triangle_4(a, h, text):
    s = (1 / 2) * a * h
    output_s = dict(result=text, triangle_parameter_a=a, triangle_parameter_h=h, out=s)
    print(output_s)             # не бажана структура відсутній обмежувач return


def area_triangle_5(a, h):
    s = (1 / 2) * a * h
    return s, a, h               # не бажана структура - множинна структура вихідних параметрів


def area_triangle_6():           # не бажана структура - неявне визначення параметрів РЕР: "явне краще ніж неявне"
    s = (1 / 2) * a * h
    return s


#------------------------- виклик функцій ---------------------------------

text = 'Площа трикутника_2'
a = 10.0
h = 22.0

area_triangle_1(a, h, text)

area_triangle_1(10.0, 22.0, 'Площа трикутника_3')

print('Площа трикутника_4=', area_triangle_2(a, h))

print('Площа трикутника_5=', area_triangle_3(a, h))


print('Площа трикутника_6=', area_triangle_4(a, h, text))

print('Площа трикутника_7=', area_triangle_5(a, h))

print('Площа трикутника_8=', area_triangle_6())




def myFun(*argv):                # структура з довільною кількістю аргументів
    print('*argv =', *argv[0])
    for arg in argv:
        print(arg)
    return


def area_triangle_7(*args):     # структура з довільною кількістю аргументів
    s = (1 / 2) * args[0] * args[1]
    return s

'''
Структура із довільною кількістю ключів - розібратись самостійно

'''

def print_kwargs(**kwargs):     # структура з довільною кількістю ключів
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


#-----------------------------------------------------------------


'''
Сегмент коду, що підлягає "огортанню" функціональним механізмом
'''

text = 'Площа трикутника_1'
a = 10.0
h = 22.0
s = (1 / 2) * a * h
output_s = dict(result=text, triangle_parameter_a=a, triangle_parameter_h=h, out=s)
print(output_s)



#------------------------- виклик функцій ---------------------------------

text = 'Площа трикутника_2'
a = 10.0
h = 22.0

area_triangle_1(a, h, text)

area_triangle_1(10.0, 22.0, 'Площа трикутника_3')

print('Площа трикутника_4=', area_triangle_2(a, h))

print('Площа трикутника_5=', area_triangle_3(a, h))

print('Площа трикутника_6=', area_triangle_4(a, h, text))

print('Площа трикутника_7=', area_triangle_5(a, h))

print('Площа трикутника_8=', area_triangle_6())

myFun('Вітаю', 'долучайтесь', 'до', 'функцій')

print('Площа трикутника_9=', area_triangle_7(10.0, 22.0))


print_kwargs(first='Долучайтесь', mid='до', last='функцій')

