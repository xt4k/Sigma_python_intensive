
'''
Область видимості функції - на рівні змінних
Scopes, LEGB Rule
https://realpython.com/python-scope-legb-rule/
https://medium.com/@ahmedfgad/python-scopes-and-the-legb-rule-d37bf3277e2c

'''


#---------- Local --------------
def func_local() -> None:
    a = 1
    print('a=', a)


#----- Enclosed (nonlocal) -----
def func_non_local() -> None:
    some_variable = 1
    
    def inner_func():
        nonlocal some_variable  # то маємо Built-in – вбудовану змінну
        some_variable = 2
        return some_variable


    print('inner_func() = ', inner_func())
    print('some_variable = ', some_variable)

    return


#---------- Global -------------
global_variable = 1

def func_for_global() -> None:
    global global_variable
    global_variable = 2
    print(global_variable)



print('-------------- локальні змінні ---------------------')

a = 2
func_local()
print('a=', a)


print('--------- закриті - нелокальні змінні --------------')
func_non_local()

print('--------------- глобальні змінні -------------------')
func_for_global()
print(global_variable)
