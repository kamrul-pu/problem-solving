"""
Given an array ‘arr’ of integer numbers, ‘arr[i]’ represents the number of pages in the ‘i-th’ book.
There are ‘m’ number of students, and the task is to allocate all the books to the students.

Allocate books in such a way that:
1. Each student gets at least one book.
2. Each book should be allocated to only one student.
3. Book allocation should be in a contiguous manner.

You have to allocate the book to ‘m’ students such that the maximum number of pages assigned to a student is minimum.

If the allocation of books is not possible, return -1.
"""

from typing import List


def f(arr: List[int], n: int, pages: int) -> int:
    """
    Helper function to determine how many students are needed
    to allocate books such that no student gets more than 'pages' pages.

    Args:
    - arr: List of integers representing pages in each book.
    - n: Integer representing the number of books.
    - pages: Integer representing the maximum pages a student can get.

    Returns:
    - int: Number of students required to allocate books with the given 'pages' constraint.
    """
    student: int = 1  # Number of students needed
    pages_student = 0  # Pages allocated to the current student

    for i in range(n):
        if pages_student + arr[i] <= pages:
            pages_student += arr[i]  # Allocate pages to current student
        else:
            student += 1  # Increment student count
            pages_student = arr[i]  # Start allocating pages to the next student

    return student


def findPages(arr: List[int], n: int, m: int) -> int:
    """
    Function to find the minimum possible maximum pages that can be allocated
    to any student while ensuring each student gets at least one book.

    Args:
    - arr: List of integers representing pages in each book.
    - n: Integer representing the number of books.
    - m: Integer representing the number of students.

    Returns:
    - int: Minimum possible maximum pages that can be allocated to any student,
           or -1 if it's not possible to allocate books to students as per the given constraints.
    """
    if m > n:
        return -1  # If there are more students than books, it's not possible

    mx: int = arr[0]  # Maximum pages in any single book
    s: int = arr[0]  # Total sum of pages in all books

    # Calculate the maximum and sum of pages in the book array
    for i in range(1, n):
        mx = max(mx, arr[i])
        s += arr[i]

    lo, hi = mx, s  # Binary search bounds for the maximum pages

    while lo <= hi:
        mid: int = (lo + hi) // 2  # Middle value of current search range
        cnt: int = f(arr, n, mid)  # Calculate number of students needed for 'mid' pages

        if cnt > m:
            lo = mid + 1  # If more students are needed, increase 'mid'
        else:
            hi = mid - 1  # If fewer or exactly 'm' students are needed, decrease 'mid'

    return lo  # Return the minimum possible maximum pages


# Example usage
n: int = 4
m: int = 2
arr: List[int] = [12, 34, 67, 90]

print(findPages(arr, n, m))
