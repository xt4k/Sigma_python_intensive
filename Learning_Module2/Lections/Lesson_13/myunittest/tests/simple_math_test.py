'''
Приклад тесту з модулем unittest - файл simple_math_test.py
Об'єкт тестування: simple_math.py

'''


import unittest

from Learning_Module2.Lections.Lesson_13.myunittest.mymath.simple_math import add, division


class SimpleMathTests(unittest.TestCase):


    def test_add_one_and_two_is_three(self):    # назва тесту має включати його логіку через Underscore

        '''
        Тестуванню підлягає семантика / логіка роботи сутності:
        якщо структура сутності "важка" - у т.ч. через невиконання РЕР - тестування ускладнюється,
        кількість тестів - збільшується, оскільки тестами бажано покрити усі розгалудження логіки;
        unit test -
        unit test hardcode - структура, зміна параметрів повинна відбуватись всередині тесту;
        unit test має писати розробник коду.
        '''

        # AAA - СТРУКТУРА тесту регламентується правилом 3А

        # arrange   -    вхідні дані А1
        a = 1
        b = 2

        # act      -  дія над вхідними даними А2
        result = add(a, b)

        # assert   - твердження, щодо результату А3
        '''
        перелік методів self.assert*** - для контролю тверджень див. за посиланням
        https://www.pythontutorial.net/python-unit-testing/python-unittest-assert/        
        '''
        self.assertEqual(result, 3)                 # логіка твердження: result == 3

    def test_division_four_by_two_is_two(self):
        a = 4
        b = 2

        result = division(a, b)

        self.assertEqual(result, 2)

    def test_division_throws_zero_division_exception(self):     # тест на контроль виключення
        a = 1
        b = 0

        self.assertRaises(ZeroDivisionError, division, a, b)    # синтаксис контролю виключення


if __name__ == '__main__':

    # SimpleMathTests_1 = SimpleMathTests()
    # SimpleMathTests_1.test_add_one_and_two_is_three()
    # SimpleMathTests_1.test_division_four_by_two_is_two
    # SimpleMathTests_1.test_division_throws_zero_division_exception

    unittest.main()