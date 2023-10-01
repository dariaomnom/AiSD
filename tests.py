import pytest
from lb1 import check

def test1():
    assert str(check([0,1,2,3,4,5,6,7], [1,3,5,7])) == "[0] [2] [4, 6]"

def test2():
    assert str(check([2, 4, 6, 8, 125], [6, 8])) == "[2, 4] [125]"

def test3():
    assert str(check([12, 36], [12, 36])) == ""

def test4():
    assert str(check([1, 2, 3, 4, 5] * 10, [1, 2, 3, 4] * 10, 10)) == "5 5 5 5 5 5 5 5 5 5"

def test5():
    assert str(check([1, 3, 6, 9] * 4, [1, 3, 9] * 4 + [6] * 3, 5)) == "6"

def test6():
    assert str(check([], [])) == ''