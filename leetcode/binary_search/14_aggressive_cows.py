"""
You are given an array 'arr' consisting of 'n' integers which denote the position of a stall.

You are also given an integer 'k' which denotes the number of aggressive cows.

You are given the task of assigning stalls to 'k' cows such that the minimum distance between
any two of them is the maximum possible.

Print the maximum possible minimum distance.
"""

from typing import List


def can_place(stalls: List[int], dist: int, cows: int) -> bool:
    """
    Helper function to check if it's possible to place 'cows' cows in 'stalls' such that
    the minimum distance between any two cows is at least 'dist'.

    Args:
    - stalls: List of integers representing positions of stalls, sorted in non-decreasing order.
    - dist: Integer representing the minimum required distance between any two cows.
    - cows: Integer representing the number of cows to place.

    Returns:
    - bool: True if it's possible to place 'cows' cows with at least 'dist' distance apart, False otherwise.
    """
    cnt: int = 1  # Number of cows placed
    last: int = stalls[0]  # Position of the last placed cow

    for i in range(1, len(stalls)):
        if stalls[i] - last >= dist:
            cnt += 1
            last = stalls[i]

    return cnt >= cows


def brute(stalls: List[int], k: int) -> int:
    """
    Brute-force approach to find the maximum possible minimum distance between cows.

    Args:
    - stalls: List of integers representing positions of stalls, sorted in non-decreasing order.
    - k: Integer representing the number of cows to place.

    Returns:
    - int: Maximum possible minimum distance between cows.
    """
    n: int = len(stalls)
    mn: int = stalls[0]
    mx: int = stalls[n - 1]

    for dist in range(1, (mx - mn + 1)):
        if can_place(stalls, dist, k):
            continue
        else:
            return dist - 1


def optimal(stalls: List[int], k: int) -> int:
    """
    Optimized binary search approach to find the maximum possible minimum distance between cows.

    Args:
    - stalls: List of integers representing positions of stalls, sorted in non-decreasing order.
    - k: Integer representing the number of cows to place.

    Returns:
    - int: Maximum possible minimum distance between cows.
    """
    n: int = len(stalls)
    mn: int = stalls[0]
    mx: int = stalls[n - 1]
    lo, hi = 1, mx - mn + 1
    ans: int = 1

    while lo <= hi:
        mid: int = (lo + hi) // 2
        if can_place(stalls, mid, k):
            ans = mid  # Update the result if current mid can place 'k' cows
            lo = mid + 1  # Try for a larger minimum distance
        else:
            hi = mid - 1  # Try for a smaller minimum distance

    return ans


def aggressiveCows(stalls: List[int], k: int) -> int:
    """
    Main function to solve the problem of assigning stalls to cows such that the minimum
    distance between any two cows is maximized.

    Args:
    - stalls: List of integers representing positions of stalls, sorted in non-decreasing order.
    - k: Integer representing the number of cows to place.

    Returns:
    - int: Maximum possible minimum distance between cows.
    """
    stalls.sort()  # Sort stalls in non-decreasing order
    # Uncomment to use the brute-force approach
    # return brute(stalls, k)
    # Use the optimal binary search approach
    return optimal(stalls, k)


if __name__ == "__main__":
    stalls: List[int] = [87, 93, 51, 81, 68, 99, 59]
    k: int = 4
    print(aggressiveCows(stalls, k))
