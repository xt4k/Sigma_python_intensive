
'''
Базові основи з формування функцій
'''


#------------------------- опис функцій ---------------------------------

def area_triangle_1(a, h, text):
    s = (1 / 2) * a * h
    output_s = dict(result=text, triangle_parameter_a=a, triangle_parameter_h=h, out=s)
    print(output_s)
    return output_s

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

test_1 = area_triangle_1(a, h, text)

test_2 = area_triangle_1(10.0, 22.0, 'Площа трикутника_3')
