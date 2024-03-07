"""
K th element in the two sorted.
"""

import time


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took " + str((end - start) * 1000) + " miliseconds")
        return result

    return wrapper


class Solution:
    @time_it
    def kth_element(self, a: list[int], b: list[int], k: int) -> int:
        i: int = 0
        j: int = 0
        cnt: int = 0
        element: int = -1
        while i < len(a) and j < len(b):
            if cnt == k:
                return element
            if a[i] < b[j]:
                element = a[i]
                i += 1
            else:
                element = b[j]
                j += 1
            cnt += 1
        # remaining element in first array
        while i < len(a):
            if cnt == k:
                return element
            element = a[i]
            i += 1
            cnt += 1

        # remainig element in the second array
        while j < len(b):
            if cnt == k:
                return element
            element = b[j]
            j += 1
            cnt += 1

        return 0

    @time_it
    def kth_element_optimal(self, a: list[int], b: list[int], k: int):
        n1, n2 = len(a), len(b)
        # if n1 is bigger swap the arrays:
        if n1 > n2:
            return self.kth_element_optimal(b, a, k)

        n = n1 + n2  # total length
        left = k  # length of left half
        # apply binary search:
        low, high = max(0, k - n2), min(k, n1)
        while low <= high:
            mid1 = (low + high) // 2
            mid2 = left - mid1
            # calculate l1, l2, r1, and r2;
            l1, l2, r1, r2 = float("-inf"), float("-inf"), float("inf"), float("inf")
            if mid1 < n1:
                r1 = a[mid1]
            if mid2 < n2:
                r2 = b[mid2]
            if mid1 - 1 >= 0:
                l1 = a[mid1 - 1]
            if mid2 - 1 >= 0:
                l2 = b[mid2 - 1]

            if l1 <= r2 and l2 <= r1:
                return max(l1, l2)

            # eliminate the halves:
            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1
        return 0  # dummy statement

    def print_arr(self, arr: list[int]) -> None:
        print(arr, sep=" ")


if __name__ == "__main__":
    arr1 = [2, 3, 6, 7, 9]
    arr2: list[int] = [1, 4, 8, 10]
    solution = Solution()
    solution.print_arr(arr1)
    solution.print_arr(arr2)
    print(solution.kth_element(arr1, arr2, 4))
    print(solution.kth_element_optimal(arr1, arr2, 4))
