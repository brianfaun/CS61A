"""Optional questions for Lab 1"""

# While Loops

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    total = n
    if k == 0:
        return 1
    while k > 1:
        total = total * (n-1)
        n -= 1
        k -= 1
    return total


            
def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    
    second_to, last = 0, 0
    while n > 10:
        last = n % 10
        second_to = n // 10
        if second_to == 8:
            if last == 8:
                return True
    return False
    

""" 
python3 ok -q falling
python3 ok -q double_eights
"""
