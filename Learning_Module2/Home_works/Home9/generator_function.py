from Learning_Module2.Home_works.Home9.Generator.fibonacci_function_generator import fib_generator

my_gen = fib_generator(15)

if __name__ == '__main__':

    print("function generator begin")
    print(my_gen)
    print(type(my_gen))
    for x in my_gen:
        print(x)
    print("function generator end")
