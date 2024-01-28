class Fibonacci:
    """
    Class to implement an iterator for fibonacci numbers
    """
    def __init__(self, n):
        self.a = 0
        self.b = 1
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == 0:
            raise StopIteration

        a = self.a
        b = self.b
        self.a = b
        self.b = a + b
        self.n -= 1
        return a