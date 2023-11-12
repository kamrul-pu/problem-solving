"""Number of available subarray with the given xor k"""


class Solution:
    def __init__(self, arr1: list[int], arr2: list[int]) -> None:
        self.arr1 = arr1
        self.arr2 = arr2

    def merge_two_sorted_arr(self) -> None:
        # using one extra array
        n = len(self.arr1)
        m = len(self.arr2)
        i: int = 0
        j: int = 0
        k: int = 0
        # declare a temp array to store result
        temp = [0] * (n + m)
        print(temp)
        while i < n and j < m:
            if self.arr1[i] < self.arr2[j]:
                temp[k] = self.arr1[i]
                i += 1
            else:
                temp[k] = self.arr2[j]
                j += 1
            k += 1
        while i < n:
            temp[k] = self.arr1[i]
            k += 1
        while j < m:
            temp[k] = self.arr2[j]
            k += 1
            j += 1
        # using slicing
        # self.arr1 = temp[:n]
        # self.arr2 = temp[n:]
        # using loop
        for i in range(k):
            if i >= n:
                self.arr2[i - n] = temp[i]
            else:
                self.arr1[i] = temp[i]

    def swap_if_greater(self, ind1: int, ind2: int) -> None:
        if self.arr1[ind1] > self.arr2[ind2]:
            self.arr1[ind1], self.arr2[ind2] = self.arr2[ind2], self.arr1[ind1]

    def merge_two_sorted_optimal1(self) -> None:
        # get the length of the two arra
        n: int = len(self.arr1)
        m: int = len(self.arr2)
        # using two pointer p1 will be the last element of the first array
        # p2 will be the first element of the second array
        p1: int = n - 1
        p2: int = 0
        while p1 >= 0 and p2 < m:
            if self.arr1[p1] > self.arr2[p2]:
                # swap the elemnt
                self.arr1[p1], self.arr2[p2] = self.arr2[p2], self.arr1[p1]
                p1 -= 1
                p2 += 1
            else:
                break
        # now sort the two array
        self.arr1.sort()
        self.arr2.sort()

    def merge_two_sorted_optimal2(self) -> None:
        # using gap method of shell sort
        n: int = len(self.arr1)
        m: int = len(self.arr2)
        tl: int = n + m  # tl = total length n+m
        # taking ceil value 9//2 = 4(int) + 9%2=1 4+1 = 5
        gap: int = (tl // 2) + (tl % 2)
        while gap > 0:
            # Place 2 pointers:
            left = 0
            right = left + gap
            while right < tl:
                # case 1: left in arr1[]
                # and right in arr2[]:
                if left < n and right >= n:
                    self.swap_if_greater(left, right - n)
                # case 2: both pointers in arr2[]:
                elif left >= n:
                    self.swap_if_greater(left - n, right - n)
                # case 3: both pointers in arr1[]:
                else:
                    self.swap_if_greater(left, right)
                left += 1
                right += 1
            # break if iteration gap=1 is completed:
            if gap == 1:
                break
            # Otherwise, calculate new gap:
            gap = (gap // 2) + (gap % 2)

    def print_arr(self) -> None:
        print("array 1:", self.arr1, sep=" ")
        print("array 2:", self.arr2, sep=" ")
        print()


if __name__ == "__main__":
    arr1 = [1, 3, 5, 7]
    arr2 = [0, 2, 6, 8, 9]
    solution = Solution(arr1, arr2)
    solution.print_arr()
    # solution.merge_two_sorted_arr()
    solution.merge_two_sorted_optimal2()
    solution.print_arr()
