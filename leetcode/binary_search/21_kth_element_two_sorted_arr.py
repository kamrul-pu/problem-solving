"""
You're given two sorted arrays 'arr1' and 'arr2' of size 'n' and 'm' respectively and an element 'k'.

Find the element that would be at the 'kth' position of the combined sorted array.

Position 'k' is given according to 1 - based indexing, but arrays 'arr1' and 'arr2' are using 0 - based indexing.s
"""

from typing import List


def better(arr1: List[int], n: int, arr2: List[int], m: int, k: int) -> int:
    k -= 1  # Adjust k to 0-based index
    total: int = n + m
    i = j = ind = 0
    element = -1

    # Traverse through both arrays to find the k-th element
    while i < n and j < m:
        if arr1[i] <= arr2[j]:
            if ind == k:
                element = arr1[i]
                return element
            i += 1
        else:
            if ind == k:
                element = arr2[j]
                return element
            j += 1
        ind += 1

    # Handle remaining elements in arr1
    while i < n:
        if ind == k:
            element = arr1[i]
            return element
        i += 1
        ind += 1

    # Handle remaining elements in arr2
    while j < m:
        if ind == k:
            element = arr2[j]
            return element
        j += 1
        ind += 1

    return element  # Return the k-th element found


def optimal(arr1: List[int], n: int, arr2: List[int], m: int, k: int) -> int:
    # Ensure arr1 is smaller or equal in size compared to arr2
    if n > m:
        return optimal(arr2, m, arr1, n, k)

    low, high = max(0, k - m), min(k, n)
    total = n + m

    # Binary search to find the correct partitioning of arr1 and arr2
    while low <= high:
        mid1 = (low + high) // 2
        mid2 = k - mid1  # Calculate mid2 based on mid1

        # Handle edge cases for out-of-bound indices
        l1 = arr1[mid1 - 1] if mid1 > 0 else float("-inf")
        r1 = arr1[mid1] if mid1 < n else float("inf")
        l2 = arr2[mid2 - 1] if mid2 > 0 else float("-inf")
        r2 = arr2[mid2] if mid2 < m else float("inf")

        # Check conditions for finding the correct partition
        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)
        elif l1 > r2:
            # Adjusting the binary search range
            high = mid1 - 1
        else:
            # Adjusting the binary search range
            low = mid1 + 1

    # Return a default value if arrays are empty or no k-th element found
    return -1


def kthElement(arr1: List[int], n: int, arr2: List[int], m: int, k: int) -> int:
    """
    Wrapper function to find the k-th element using the optimal approach.

    Args:
    - arr1 (List[int]): First sorted array
    - n (int): Size of arr1
    - arr2 (List[int]): Second sorted array
    - m (int): Size of arr2
    - k (int): 1-based index of the element to find

    Returns:
    - int: The k-th element in the combined sorted array
    """
    return optimal(arr1, n, arr2, m, k)


# Example usage:
arr1: List[int] = [2, 3, 6, 7, 9]
n: int = 5
arr2: List[int] = [1, 4, 8, 10]
m: int = 4
k: int = 4
print(kthElement(arr1, n, arr2, m, k))
