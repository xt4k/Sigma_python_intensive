'''
Testset for pytest.pure_division()
testcases:
1) 12 divided to 3 without left -> true
2) 12 divided to 5 without left -> false
3) 1 divide to 0 return ZeroDivisionException
4) 0 divide to 0 return ZeroDivisionException
5) 0 divide to 5 -> true
6) '1' divide to 2 return TypeError
7) 1 divide to '2' return TypeError
8) 1 divide to None return TypeError
9)  None divide to 1 return TypeError
'''

import pytest
from Learning_Module1.Home_works.Home2.fizz_buzz import pure_division
def test_divided_true():
    assert pure_division(12,3)


def test_divided_false():
    assert not pure_division(12, 5)


def test_divided_zero_exception():
    with pytest.raises(ZeroDivisionError):
        assert pure_division(1, 0)


def test_zero_divided_zero_exception():
    with pytest.raises(ZeroDivisionError) as e_info:
        assert pure_division(0, 0)


def test_zero_divided_true():
    assert pure_division(0, 5)


def test_wrong_input_exception():
    with pytest.raises(TypeError):
        assert pure_division("1", 2)


def test_wrong_base_exception():
    with pytest.raises(TypeError):
        assert pure_division(1, "2")



def test_element_none_exception():
    with pytest.raises(TypeError):
        assert pure_division(1, None)

def test_base_none_input_exception():
    with pytest.raises(TypeError):
        assert pure_division(None, 1)
