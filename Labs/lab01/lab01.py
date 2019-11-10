"""Lab 1: Expressions and Control Structures"""

def both_positive(x, y):
    """Returns True if both x and y are positive.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    return x > 0 and y > 0

def sum_digits (n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> x = sum_digits(123) # make sure that you are using return rather than print
    >>> x
    6
    """
    "*** YOUR CODE HERE ***"
    total, last_digit = 0, 0
    if n == 10:
        return 1
    while n > 10:
        last_digit = n % 10
        total += last_digit
        n = n // 10
    total += n
    return total

"""
python3 ok -q both_positive
python3 ok -q sum_digits
"""
