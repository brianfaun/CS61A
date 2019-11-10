HW_SOURCE_FILE = 'hw03.py'

#############
# Questions #
#############

def num_sevens(n):
    """Returns the number of times 7 appears as a digit of n.

    >>> num_sevens(3)
    0
    >>> num_sevens(7)
    1
    >>> num_sevens(7777777)
    7
    >>> num_sevens(2637)
    1
    >>> num_sevens(76370)
    2
    >>> num_sevens(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_sevens',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n < 10:
        if n == 7:
            return 1
        return 0
    else:
        return num_sevens (n // 10) + num_sevens(n % 10)

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"

    # iteration
    """
    element, number = 1, 1
    change = 1
    while element < n:
        if (num_sevens(element) != 0) or (element % 7 == 0):
            change *= -1
        element, number = element + 1, number + change
    return number
    """

    #recursive 2 (X)
    def helper(element, number, change):
        if element >= n:
            return number
        if (num_sevens(element) != 0) or (element % 7 == 0):
            return helper (element + 1, number + (-1 * change), -1 * change)
        return helper(element + 1, number + change, change)
    return helper(1, 1, 1)


    #recursive 1
    """
    def reversal_count (element):
        # Counts how many times the counting up to index Element reverses
        if element < 7:
            return 0
        elif (num_sevens(element) != 0) or (element % 7 == 0):
            return reversal_count(element - 1) + 1
        return reversal_count(element - 1)

    if n <= 7:
        return n
    if reversal_count(n-1) % 2 != 0:
        return pingpong(n-1) - 1
    return pingpong (n-1) + 1
    """

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_change', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    def maxpow (n, start):
        """ Returns the exponent of power of 2 for highest coin included in Amount without using while """
        if pow (2, start) <=  n:
            return maxpow (n, start + 1)
        else:
            return start -1

    def count_partitions (n, m):
        """ Count the ways to partition N with parts up to M """
        if n == 0:
            return 1
        elif n < 0:
            return 0
        elif m == 0:
            return 1
        else:
            return count_partitions(n-pow(2,m), m) + count_partitions(n, m - 1)

    big_coin = maxpow (amount, 0)
    return count_partitions (amount, big_coin)

def flatten(lst):
    """Returns a flattened version of lst.

    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]     # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x # Ensure x is not mutated
    [1, [2, 3], 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    >>> x
    [[1, [1, 1]], 1, [1, 1]]
    """
    "*** YOUR CODE HERE ***"
    """ (final-1)
    while i < len(lst) :
        if type (lst[i : i+1][0] ) == list:
            newlist = lst[i : i+1][0]
            flattened += newlist
        else:
            flattened += lst[i : i+1]
        i += 1
    return flattened
    """
    final ,flattened = [], []
    i, recount = 0, 0

    while i < len(lst) :
        if type (lst[i : i+1][0] ) == list:
            newlist = lst[i : i+1][0]
            flattened += newlist
        else:
            flattened += lst[i : i+1]
        i += 1
    #return flattened

    while recount < len(flattened) :
        if type (flattened[recount : recount+1][0] ) == list:
            newlist = flattened[recount : recount+1][0]
            final += newlist
        else:
            final += flattened[recount : recount+1]
        recount += 1
    return final


###################
# Extra Questions #
###################

def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return 'YOUR_EXPRESSION_HERE'
