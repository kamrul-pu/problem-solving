"""
You are given two positive integers 'n' and 'm'. You have to return the 'nth' root of 'm', i.e. 'm(1/n)'.
If the 'nth root is not an integer, return -1.

Note:
'nth' root of an integer 'm' is a number, which, when raised to the power 'n', gives 'm' as a result.
"""


def NthRoot(n: int, m: int) -> int:
    """
    Computes the nth root of m using binary search.

    Args:
    - n: Positive integer (the root index)
    - m: Positive integer (the number whose root is to be found)

    Returns:
    - Integer: The nth root of m if it exists and is an integer, otherwise -1.
    """
    lo, hi = 1, m

    # Binary search to find the nth root of m
    while lo <= hi:
        mid: int = (lo + hi) // 2
        res: int = mid**n

        if res == m:
            return mid  # Found exact nth root
        elif res > m:
            hi = mid - 1  # Adjusting the upper bound
        else:
            lo = mid + 1  # Adjusting the lower bound

    return -1  # If no exact nth root is found, return -1


# Example usage:
print(NthRoot(n=3, m=27))  # Output: 3 (since 3^3 = 27)
