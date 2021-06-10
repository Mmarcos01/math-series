def fibonacci(n):
    """
    This function will take one parameter (n) and return the nth value in the fibonacci series, starting at: 0, 1. (the nth value is the sum of the two previous values in the series)
    """
    if n <= 1:
        return n
   # recursion:
    return (fibonacci(n - 1) + fibonacci(n-2))


def lucas(n):
    """
        This function will take one parameter (n) and return the nth value in the lucas series starting at: 2, 1. (the nth value is the sum of the two previous values in the series)
    """
    if n == 0:
        return 2
    elif n == 1:
        return n
    return (lucas(n - 1) + lucas(n-2))
