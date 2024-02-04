import pytest
from Learning_Module1.Home_works.Home2.fizz_buzz import analysis

fizz = "Fizz"
buzz = "Buzz"

'''
Testset for pytest.analysis()
testcases:
1) 15 divided to 3 and 5 without left -> "FizzBuzz"
2) 12 divided to 3 without left but divided to 5 with left -> "Fizz" 
3) 10 divided to 5 without left but divided to 3 with left -> "Buzz"
4) 7 -> 7
5) 0 -> "FizzBuzz"
6) 'q' -> return TypeError
7) None -> return TypeError
'''


def test_fizzbuzz():
    assert analysis(15) == fizz + buzz


def test_fizz():
    assert analysis(12) == fizz


def test_buzz():
    assert analysis(10) == buzz


def test_element():
    assert analysis(7) == 7


def test_zero():
    assert analysis(0) == fizz + buzz


def test_type_error():
    with pytest.raises(TypeError):
        assert analysis("q")


def test_none():
    with pytest.raises(TypeError):
        assert analysis(None)