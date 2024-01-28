from Learning_Module2.Home_works.Home9.Generator.fibonacci_expression_generator import fib_expression


def main():
    for i in fib_expression(10):
        print(i)


if __name__ == "__main__":
    main()

    print("one by one")
    gen_exp =fib_expression(9)

    print(next(gen_exp))
    print(next(gen_exp))
    print(next(gen_exp))
    print(next(gen_exp))
    print(next(gen_exp))

    print(next(gen_exp))
    print(next(gen_exp))
    print(next(gen_exp))



