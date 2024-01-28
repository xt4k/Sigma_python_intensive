def fib_generator(steps):
    """
    Implement generator for fibonacci numbers here
    """
    a,b = 0, 1
    for _ in range(steps):
        # print("step", step_number - n, "fib number: ",a + b)
        # yield a + b
        # temp_a = a
        # a = b
        # b = temp_a + b
        yield a
        a, b = b, a + b
       # n -= 1
    #pass
    raise StopIteration