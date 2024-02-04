'''
Розрахунок коренів квадратного рівняння
'''

from math import sqrt

import matplotlib.pyplot as plt
import numpy as np


def square_eq_solver(a, b, c):
   result = []
   discriminant = b * b - 4 * a * c

   if discriminant == 0:
       result.append(-b / (2 * a))
   elif discriminant > 0:
       result.append((-b + sqrt(discriminant)) / (2 * a))
       result.append((-b - sqrt(discriminant)) / (2 * a))

   return result

def show_result(data):
   if len(data) > 0:
       for index, value in enumerate(data):
           print(f'Корень номер {index+1} дорівнює {value:.02f}')
   else:
       print('Рівняння із заданими параметрами не має коренів')

def show_result_image(a, b, c):
    x = np.linspace(-100, 100, 1000)
    y = a * x ** 2 + b * x + c
    fig, ax = plt.subplots()
    plt.grid(True)
    ax.plot(x, y)
    plt.show()


def main():
   a, b, c = map(int, input('Задайте параметра рівняння ax2 + bx + c через пробіл: a b c: ').split())
   show_result_image(a, b, c)
   result = square_eq_solver(a, b, c)
   show_result(result)

if __name__ == '__main__':
   main()
