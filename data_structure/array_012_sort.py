class Solution:
    def __init__(self, arr) -> None:
        self.arr = arr

    def sort1(self):
        # Brute Force solution TC O(n^2) Space O(1)
        count_0 = count_1 = count_2 = 0
        # Count number of 0 1 and 2
        for x in self.arr:
            if x == 0:
                count_0 += 1
            elif x == 1:
                count_1 += 1
            else:
                count_2 += 1

        k = 0
        # fill the element to the array
        # fill zero
        while count_0:
            self.arr[k] = 0
            k += 1
            count_0 -= 1
        # fill 1
        while count_1:
            self.arr[k] = 1
            k += 1
            count_1 -= 1

        # Fill 2
        while count_2:
            self.arr[k] = 2
            k += 1
            count_2 -= 1

    def sort2(self):
        # Using Dutch National Flag Algorithm
        # Three pointer approach. TC O(n) Space O(1)
        low = 0
        mid = 0
        high = len(self.arr) - 1
        while mid <= high:
            if self.arr[mid] == 0:
                # Swap mid with low
                self.arr[low], self.arr[mid] = self.arr[mid], self.arr[low]
                low += 1  # Increment low and mid
                mid += 1
            elif self.arr[mid] == 1:
                mid += 1  # Increment mid
            else:
                # Swap high with mid
                self.arr[mid], self.arr[high] = self.arr[high], self.arr[mid]
                # Decrement high
                high -= 1

    def print_arr(self):
        print(self.arr)


if __name__ == "__main__":
    arr = list(map(int, input().split(" ")))
    solution = Solution(arr)
    solution.print_arr()
    solution.sort2()
    solution.print_arr()
