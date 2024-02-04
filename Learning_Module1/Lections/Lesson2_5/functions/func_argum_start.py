
'''
Способи передачі параметрів до функції - аргументи через інтерфейс (специфікацію)
'''


# Аргумент за замовчуванням -
# це параметр, який приймає значення за замовчуванням,
# якщо значення не вказано у виклику функції для цього аргументу.

def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)
    return

myFun(10)


# Аргументи ключових слів
# Ідея полягає в тому, щоб дозволити  вказувати назву аргументу зі значеннями,
# щоб не потрібно було запам’ятовувати порядок параметрів.

def student(firstname, lastname):
    print(firstname, lastname)

student(firstname='Python_1', lastname='C#_1')
student(lastname='C#_2', firstname='Python_2')


# Позиційні аргументи
# Змінні чітко визначаються позицією

def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)


nameAge("Python_1", 27)
nameAge(27, "Python_1")

