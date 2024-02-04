
'''
Приклад організації інфраструктури проекту python

'''

import package_functions
from package_functions import module_1, module_2

from package_classes import (
    MyClass_my_cv_dict,
    MyClass_my_cv_file_w,
    MyClass_my_cv_file_r,
    MyClass_f_digit_detector
)


def package_functions_main_def():
    print('--------------------- звернення до module_1 ---------------')
    text = 'Площа трикутника'
    a = 10.0
    h = 22.0
    test_1 = module_1.area_triangle(a, h)
    print(text, ' S =', test_1, '\n')

    print('--------------------- звернення до module_2 ---------------')
    module_2.myFun(10)
    module_2.student(firstname='Python_1', lastname='C#_1')
    module_2.student(lastname='C#_2', firstname='Python_2')
    module_2.nameAge("Python_1", 27)
    module_2.nameAge(27, "Python_1")

    print('--------------------- звернення до module_3 ---------------')
    text = 'Площа трикутника'
    a = 100.0
    h = 22.0
    in_s = dict(result=text, triangle_parameter_a=a, triangle_parameter_h=h)
    package_functions.module_3.example_dict(in_s)
    print('result = ', package_functions.module_3.example_dict(in_s)['result'])
    print('triangle_parameter_a = ', package_functions.module_3.example_dict(in_s)['triangle_parameter_a'])
    print('triangle_parameter_h = ', package_functions.module_3.example_dict(in_s)['triangle_parameter_h'])
    print('out = ', package_functions.module_3.example_dict(in_s)['out'])

    return


def package_class_main_def():
    obj_1 = MyClass_my_cv_dict()
    obj_2 = MyClass_my_cv_file_w()
    obj_3 = MyClass_my_cv_file_r()
    obj_4 = MyClass_f_digit_detector()

    FILE_NAME = "Ivanchenko_CV.csv"
    my_cv_dict_out = obj_1.my_cv_dict()
    obj_2.my_cv_file_w(FILE_NAME, my_cv_dict_out)
    text_in = obj_3.my_cv_file_r(FILE_NAME)
    obj_4.f_digit_detector(text_in)

    return


def package_image_main_def():
    file_name_start = 'sentinel_2023.jpg'
    file_name_stop = "stop.jpg"
    file_name_filter = "stop_filter.jpg"

    print('оберіть тип перетворення!')
    print('0 - відтінки сірого')
    print('1 - серпія')
    print('2 - негатив')
    print('3 - зашумлення')
    print('4 - зміна яскравості')
    print('5 - монохромне зображення')
    print('6 - фільтр-векторизатор')
    mode = int(input('mode:'))
    if (mode == 0): Module_2.Lesson_4_9.Lesson_4_9.Lesson_4_9.package_images.Im_PIL.shades_of_gray(file_name_start, file_name_stop)
    if (mode == 1): Module_2.Lesson_4_9.Lesson_4_9.Lesson_4_9.package_images.Im_PIL.serpia(file_name_start, file_name_stop)
    if (mode == 2): Module_2.Lesson_4_9.Lesson_4_9.Lesson_4_9.package_images.Im_PIL.negative(file_name_start, file_name_stop)
    if (mode == 3): Module_2.Lesson_4_9.Lesson_4_9.Lesson_4_9.package_images.Im_PIL.noise(file_name_start, file_name_stop)
    if (mode == 4): Module_2.Lesson_4_9.Lesson_4_9.Lesson_4_9.package_images.Im_PIL.brightness_change(file_name_start, file_name_stop)
    if (mode == 5): Module_2.Lesson_4_9.Lesson_4_9.Lesson_4_9.package_images.Im_PIL.monochrome(file_name_start, file_name_stop)
    if (mode == 6): Module_2.Lesson_4_9.Lesson_4_9.Lesson_4_9.package_images.Im_PIL.contour_im(file_name_stop, file_name_filter)

    return


if __name__ == '__main__':
    # package_functions_main_def()
    # package_class_main_def()
    package_image_main_def()
