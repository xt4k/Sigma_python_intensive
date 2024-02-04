
'''

Виконав:
Homework_2, І рівень складності:

Група вимог ІІ

Група вимог ІІІ

Package                      Version
---------------------------- -----------
pip                          23.1

'''


import sys
import re

# ------------------------ homework_4 -------------------------------

def my_cv_dict () -> dict:

    '''

    :return:
    '''

    my_name = "Vasil Ivanchenko"
    my_birtn = "1998"
    age = "30"
    my_programming_languages = ["Python", "C#", "Java", "C++"]  # список
    print(my_programming_languages[0])

    my_favorite_numbers = {3, 5, 7, 12}  # множина

    my_cv_dict = dict({0: my_name,
                       1: my_birtn,
                       2: age,
                       3: my_programming_languages,
                       4: my_favorite_numbers, })  # словник

    print("My name is : ", my_cv_dict[0])
    print("My_birtn : ", my_cv_dict[1])
    print("My age is : ", my_cv_dict[2])

    print("I can solve problems, using these programming languages:")
    print(my_cv_dict[3][0])
    print(my_cv_dict[3][1])
    print(my_cv_dict[3][2])
    print(my_cv_dict[3][3])

    print("My_favorite_numbers:")
    print(my_cv_dict[4])

    print(type(my_cv_dict))
    print((my_cv_dict))

    return my_cv_dict


def my_cv_file_txt_w (my_cv_dict: dict) -> None:

    '''

    :param my_cv_dict:
    :return:
    '''

    FILE_NAME_txt = "Ivanchenko_CV.txt"
    try:
        with open(FILE_NAME_txt, "w", encoding="UTF-8") as file:
            for i in range((len(my_cv_dict))):
                file.write(f'{my_cv_dict[i]},\n')
    except PermissionError:
        print("Sorry, you have no access to this file")
    except Exception as error:
        print(f"It looks like something has happened. This is {error}")

    return

def my_cv_file_scv_w (my_cv_dict: dict) -> None:

    '''

    :param my_cv_dict:
    :return:
    '''

    FILE_NAME_csv = "Ivanchenko_CV.csv"

    my_cv_str = str(my_cv_dict)
    print(type(my_cv_str))
    print((my_cv_str))

    try:
        with open(FILE_NAME_csv, "w", encoding="UTF-8") as file:
            file.writelines(my_cv_str)
    except PermissionError:
        print("Sorry, you have no access to this file")
    except Exception as error:
        print(f"It looks like something has happened. This is {error}")

    return

def my_cv_file_scv_w_dict (my_cv_dict: dict) -> None:

    '''

    :param my_cv_dict:
    :return:
    '''

    FILE_NAME_txt_dic = "Ivanchenko_CV_dic.txt"
    try:
        with open(FILE_NAME_txt_dic, 'w') as file:
            for key, value in my_cv_dict.items():
                file.write(f'{key}, {value}\n')
    except PermissionError:
        print("Sorry, you have no access to this file")
    except Exception as error:
        print(f"It looks like something has happened. This is {error}")

    return

def my_cv_file_r (FILE_NAME: str) -> None:

    '''

    :param FILE_NAME:
    :return:
    '''

    text = []

    try:
        with open(FILE_NAME, 'r') as f:
            for j in f:
                text.append(j.strip() + " ")
    except FileNotFoundError:
        print(f'Sorry, the file {FILE_NAME} does not exist.')
        sys.exit(0)

    else:
        # ----- аналіз строки на наявність чисел / цифр операціями над строками перед цим - фільтація ---
        # https: // www.w3schools.com / python / python_ref_string.asp

        print("--- аналіз строки на наявність чисел / цифр операціями над строками перед цим - фільтація ---")
        for i in text:
            print (i, ' ', i.isdigit() )
        for i in text:
            print(i, ' ', i.isnumeric())

        # ------------- аналіз строки на наявність чисел з використанням регулярних виразів -------------
        # https://realpython.com/search?q=regular+expressions
        # https://docs.python.org/3/library/re.html
        # https: // www.tutorialspoint.com / python / python_reg_expressions.htm

        print("---------- аналіз строки на наявність чисел з використанням регулярних виразів ------------")
        digit_detector = re.findall('[0-9]+', str(text))
        print("text_in_re", text)
        print("text_out_re", digit_detector)


        print("-" * 95)

    return

if __name__ == "__main__":

    my_cv_dict_out = my_cv_dict()
    my_cv_file_txt_w(my_cv_dict_out)
    my_cv_file_scv_w(my_cv_dict_out)
    my_cv_file_scv_w_dict(my_cv_dict_out)

    my_cv_file_r("Ivanchenko_CV.txt")
    my_cv_file_r ("Ivanchenko_CV.csv")
    my_cv_file_r ("Ivanchenko_CV_dic.txt")





'''
Результат:


Резюме - якщо є бажання поділитись думками:


'''


