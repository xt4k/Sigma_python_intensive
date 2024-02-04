import pytest

from ..mymath.simple_math import add, division


def test_add_one_and_two_is_three():
    # arrange
    a = 1
    b = 2

    # act
    result = add(a, b)

    # assert
    assert result == 3                               # директива - ключове слово assert - сигналізує про pytest


def test_division_four_by_two_is_two():
    a = 4
    b = 2

    result = division(a, b)

    assert result == 2


def test_division_throws_zero_division_exception():
    a = 1
    b = 0

    with pytest.raises(ZeroDivisionError):          # контексний менеджер raises забезпечує обробку винятків в pytest
        division(a, b)                              # директива assert імплементована в raises
