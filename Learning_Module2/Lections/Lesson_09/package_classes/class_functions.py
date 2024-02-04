import sys
import re

#-------------------------- ОПИС АЛГОРИТМУ механізмами ОПП -------------------------------

#------------------------------- class формування my_cv  ---------------------------------
class MyClass_my_cv_dict:

    def my_cv_dict(self) -> dict:
        my_name = "Vasil Ivanchenko"
        my_birtn = "1998"
        age = "30"
        my_programming_languages = ["Python", "C#", "Java", "C++"]  # список

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

        return my_cv_dict

#-------------------------- class запису my_cv до файлу -------------------------------

class MyClass_my_cv_file_w:

    def my_cv_file_w(self, FILE_NAME_csv: str, my_cv_dict: dict) -> None:

        my_cv_str = str(my_cv_dict)
        try:
            with open(FILE_NAME_csv, "w", encoding="UTF-8") as file:
                file.writelines(my_cv_str)
        except PermissionError:
            print("Sorry, you have no access to this file")
        except Exception as error:
            print(f"It looks like something has happened. This is {error}")

        return


#-------------------------- class зчитування my_cv з файлу ------------------------------

class MyClass_my_cv_file_r:

    def my_cv_file_r(self, FILE_NAME: str) -> list:

        text = []
        try:
            with open(FILE_NAME, 'r') as f:
                for j in f:
                    text.append(j.strip() + " ")
        except FileNotFoundError:
            print(f'Sorry, the file {FILE_NAME} does not exist.')
            sys.exit(0)

        return text

#-------------------------- class детекціі чисел у  my_cv  ------------------------------

class MyClass_f_digit_detector:

    def f_digit_detector(self, text: list) -> None:

        print("---------- аналіз строки на наявність чисел з використанням регулярних виразів ------------")
        digit_detector = re.findall('[0-9]+', str(text))
        print("text_in_re", text)
        print("text_out_re", digit_detector)

        for i in range((len(digit_detector))):
            digit_detector[i] = str(int(digit_detector[i]) + 25)
        print("digit_detector+25", digit_detector)

        return






