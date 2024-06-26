"""
You are given an array of ‘N’ integers where each integer value is between ‘1’ and ‘N’.
Each integer appears exactly once except for ‘P’, which appears exactly twice, and ‘Q’, which is missing.

Your task is to find ‘P’ and ‘Q’ and return them respectively.
"""

from collections import defaultdict
from typing import List, Dict


def brute(a: List[int]) -> List[int]:
    n: int = len(a)
    repeating: int = float("-inf")
    missing: int = float("-inf")

    # Iterate through each integer from 1 to N
    for i in range(1, n + 1):
        cnt: int = 0

        # Count occurrences of i in the array 'a'
        for j in range(n):
            if a[j] == i:
                cnt += 1

        # Determine if 'i' is the repeating number or the missing number
        if cnt == 0:
            missing = i  # 'i' is missing if it doesn't appear in 'a'
        elif cnt == 2:
            repeating = i  # 'i' repeats twice in 'a'

    return [repeating, missing]


def better(a: List[int]) -> List[int]:
    n: int = len(a)
    hsh: Dict[int, int] = defaultdict(int)

    # Count occurrences of each integer using a dictionary
    for i in range(n):
        hsh[a[i]] += 1

    repeating: int = float("-inf")
    missing: int = float("-inf")

    # Identify the repeating and missing numbers
    for i in range(1, n + 1):
        if hsh[i] == 2:
            repeating = i  # 'i' appears twice
        elif hsh[i] == 0:
            missing = i  # 'i' does not appear at all

    return [repeating, missing]


def optimal_math(a: List[int]) -> List[int]:
    n: int = len(a)
    s: int = 0  # Sum of elements in 'a'
    s2: int = 0  # Sum of squares of elements in 'a'
    sn: int = (n * (n + 1)) // 2  # Sum of first 'n' natural numbers
    s2n: int = (
        n * (n + 1) * (2 * n + 1)
    ) // 6  # Sum of squares of first 'n' natural numbers

    # Calculate 's' and 's2' from the given array 'a'
    for i in range(n):
        s += a[i]
        s2 += a[i] * a[i]

    # Calculate x - y and (x + y) * (x - y)
    val1: int = s - sn
    val2: int = s2 - s2n
    val2 = val2 // val1

    # Solve for 'x' and 'y'
    x: int = (val1 + val2) // 2
    y: int = x - val1

    return [x, y]


def findMissingRepeatingNumbers(a: List[int]) -> List[int]:
    # Write your code here
    # Try to submit your code in O(n) Time complexity.
    # return brute(a=a)
    # return better(a=a)
    return optimal_math(a=a)


a: List[int] = [4, 3, 6, 2, 1, 1]
print(findMissingRepeatingNumbers(a=a))
