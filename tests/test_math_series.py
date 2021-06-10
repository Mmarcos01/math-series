from math_series.series import fibonacci, lucas

def test_zero_returns_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_one_returns_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_two_returns_one():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_three_returns_two():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected

def test_four_returns_three():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected

def test_five_returns_five():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected

def test_five_returns_five():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected

def test_six_returns_eight():
    actual = fibonacci(6)
    expected = 8
    assert actual == expected

def test_seven_returns_thirteen():
    actual = fibonacci(7)
    expected = 13
    assert actual == expected

def test_lucas_zero_returns_two():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_one_returns_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_two_returns_3():
    actual = lucas(2)
    expected = 3
    assert actual == expected

