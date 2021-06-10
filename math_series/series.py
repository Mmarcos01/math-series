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

# n determines which element in the series to print.
# x and y determine the first two values in the series


def sum_series(n, x=0, y=1):
    """
     Calling this function with no optional parameters will produce numbers from the fibonacci series.

     Calling it with the optional arguments 2 and 1 will produce values from the lucas numbers. 

     Other values for the optional parameters will produce other series. 
    """
    if n == 1:
      return fibonacci(1)

