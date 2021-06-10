from math_series.series import fibonacci, lucas, sum_series

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

def test_lucas_two_returns_three():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def test_lucas_three_returns_four():
    actual = lucas(3)
    expected = 4
    assert actual == expected

def test_lucas_four_returns_seven():
    actual = lucas(4)
    expected = 7
    assert actual == expected

def test_lucas_five_returns_eleven():
    actual = lucas(5)
    expected = 11
    assert actual == expected

def test_lucas_six_returns_eighteen():
    actual = lucas(6)
    expected = 18
    assert actual == expected

def test_lucas_seven_returns_twentynine():
    actual = lucas(7)
    expected = 29
    assert actual == expected

def test_sum_series_no_optionals_returns_fibonacci():
    actual = sum_series(1)
    expected = fibonacci(1)
    assert actual == expected

def test_sum_series_with_optionals_two_and_one_returns_lucas():
    actual = sum_series(1, 2, 1)
    expected = lucas(1)
    assert actual == expected
