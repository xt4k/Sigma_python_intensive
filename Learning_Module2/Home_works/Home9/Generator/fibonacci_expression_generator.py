def fib_expression(steps):
    """
    Implement generator expression function for fibonacci numbers here
    """
    a, b = 0, 1
    for _ in range(steps):
        yield a
        a, b = b, a + b
    pass
    # raise StopIteration