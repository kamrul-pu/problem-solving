"""
Median Of two sorted array.
"""
INT_MIN: int = -99999
INT_MAX: int = 99999


class Solution:
    def median(self, a, b):
        n1, n2 = len(a), len(b)
        # if n1 is bigger swap the arrays:
        if n1 > n2:
            return self.median(b, a)

        n = n1 + n2  # total length
        left = (n1 + n2 + 1) // 2  # length of left half
        # apply binary search:
        low, high = 0, n1
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
                if n % 2 == 1:
                    return max(l1, l2)
                else:
                    return (float(max(l1, l2)) + float(min(r1, r2))) / 2.0

            # eliminate the halves:
            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1
        return 0  # dummy statement

    def print_arr(self, arr: list[int]) -> None:
        print(arr, sep=" ")


if __name__ == "__main__":
    arr1 = [1, 3, 4, 7, 10, 12]
    arr2: list[int] = [2, 3, 6, 15]
    solution = Solution()
    solution.print_arr(arr1)
    solution.print_arr(arr2)
    print(solution.median(arr1, arr2))
