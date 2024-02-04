# --------------------------- Homework_8  ------------------------------------

'''

Виконав:

Homework_8

Для функції get_data(), яка повертає список днів тижня
Створіть два декоратора:

Декоратор_№1 / Обов'язковий/ short_form -> повертає скорочення днів тижня
приклад:
Коли get_data() має значення ['Monday', ..., 'Sunday'], тоді декоратор
short_form має повертати ['Mon', ..., 'Sun'].
*** Порада: знайдіть модуль `calendar` та функцію, яка підходить саме Вам.

Декоратор_№2 / Додатковий / translate(language) -> декоратор, який приймає аргумент «language».
Має перекласти назви днів тижня на мову, вказану в параметрі.
*** Порада: дізнайтеся, як працює модуль `locale`, і знайдіть функцію `setlocale`.
Ви можете вільно використовувати будь-яке інше рішення перекладу

В результаті програма повинна просто вивести на екран список, наприклад, німецькомовних скорочень днів тижня. ->
['Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa', 'So']

Декоратори та головні виклики мають бути в різних модулях!
Бажано передбачити ствоерення та використання віртуального оточення.

'''



import calendar
import locale
import sys
from functools import wraps

from pip._internal.utils import subprocess

from Learning_Module2.Home_works.Home8.decorators.short import short_form

#
#
# class translate():
#     def __init__(self, func):
#         self.function = func
#
#     def __call__(self, *args, **kwargs):
#         print("decor_sh_f")
#         print(locale.getpreferredencoding())
#         print(locale.getlocale())
#         print(locale.getdefaultlocale())
#
#        # env = os.environment.copy()
#        # env['LANG'] = 'en_US.UTF-8'
#        # subprocess.check_output(..., env=env)
#
#         try:
#             locale.setlocale(*args,**kwargs)
#         except locale.Error:
#             print('SKIP: Locale de_DE.UTF-8 is not supported on this machine')
#         result = self.function(*args, **kwargs)
#         return result
#
# #@translate #"de_DE.utf8")
# def get_data1(any_list):
#     print(any_list)
#     return list(any_list)


#@translate("de_DE.utf8")
@short_form
def get_data(any_list):
    print("initial list:\n",any_list)
    print("after modifying: ")
    return list(any_list)


if __name__ == '__main__':

    """
    Test cases:
    ['Monday', 'Friday'] -> ['Mon', 'Fri']
    ['Something', "New"] -> ['Something', "New"]
    ['Something', "New", "Tuesday"] -> ['Something', "New", "Tue"]
    """

    print(get_data(list(calendar.month_name) + list(calendar.day_name)))
    print(get_data(['Something', "New"]))
    print(get_data(['Something', "New", "Tuesday"]))
