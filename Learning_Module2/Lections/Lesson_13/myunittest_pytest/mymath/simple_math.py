
def add(a: int, b: int) -> int:
    """Calculate sum of a and b

    Args:
        a (int): first number
        b (int): second number

    Returns:
        int: sum of a and b
    """
    return a + b


def division(a: int, b: int) -> int:
    """Calculates division of a and b

    Args:
        a (int): first number
        b (int): second number

    Returns:
        int: result of division a and b
    """
    try:
        return a // b
    except ZeroDivisionError:
        raise
