"""
Given an array/list of length n, where the array/list represents the boards and each element
of the given array/list represents the length of each board. Some k numbers of painters are
available to paint these boards. Consider that each unit of a board takes 1 unit of time to paint.

You are supposed to return the area of the minimum time to get this job done of painting all the
n boards under a constraint that any painter will only paint the continuous sections of boards.
"""

from typing import List


def num_painters_needed(boards: List[int], n: int, max_length_per_painter: int) -> int:
    """
    Helper function to calculate the number of painters needed for a given max length
    each painter can handle.

    Args:
    - boards: List of integers representing lengths of boards.
    - n: Number of boards.
    - max_length_per_painter: Maximum length of boards that one painter can handle.

    Returns:
    - Number of painters required to paint all boards within the given max length constraint.
    """
    num_painters = 1  # Initially assume one painter is sufficient
    current_length = 0  # Length of boards currently assigned to the current painter

    for length in boards:
        if current_length + length <= max_length_per_painter:
            current_length += length  # Assign this board to the current painter
        else:
            num_painters += 1  # Need another painter
            current_length = length  # Assign this board to the new painter

    return num_painters


def find_minimum_time_to_paint(boards: List[int], k: int) -> int:
    """
    Function to find the minimum possible maximum pages (time) required to paint
    all the boards using a binary search approach.

    Args:
    - boards: List of integers representing lengths of boards.
    - k: Number of painters available.

    Returns:
    - Minimum possible maximum time required to paint all boards under the given constraints.
    """
    n = len(boards)
    if k > n:
        return -1  # If there are more painters than boards, it's not possible

    max_length = boards[0]  # Maximum length of any single board
    total_length = boards[0]  # Total length of all boards

    # Calculate the maximum and sum of lengths of the boards
    for length in boards[1:]:
        max_length = max(max_length, length)
        total_length += length

    lo, hi = max_length, total_length  # Binary search bounds for the maximum length

    while lo <= hi:
        mid = (lo + hi) // 2  # Middle value of current search range
        painters_needed = num_painters_needed(boards, n, mid)

        if painters_needed > k:
            lo = mid + 1  # If more painters are needed, increase the maximum length
        else:
            hi = (
                mid - 1
            )  # If fewer or exactly 'k' painters are needed, decrease the maximum length

    return lo  # Return the minimum possible maximum length (time)


# Example usage:
boards = [2, 1, 5, 6, 2, 3]
k = 2

print(find_minimum_time_to_paint(boards, k))
