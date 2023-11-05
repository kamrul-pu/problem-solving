"""Majority elements means a number appered more then n/2 times."""


class Solution:
    def __init__(self, arr) -> None:
        self.arr = arr

    def max_sum1(self) -> int:
        # Time Complexity O(n^2)
        mx = -123456
        for i in range(len(self.arr)):
            sum = self.arr[i]
            for j in range(i + 1, len(self.arr)):
                sum += self.arr[j]
                mx = max(mx, sum)

        # Comparing with zero for negetive sum
        mx = max(mx, 0)
        return mx

    def max_sum2(self) -> int:
        # Using kadan's Algorithm
        # TC O(n) Space O(1)
        mx: int = -123456
        sum: int = 0
        for i in range(len(self.arr)):
            sum += self.arr[i]
            mx = max(mx, sum)
            if sum < 0:
                sum = 0

        mx = max(mx, 0)
        return mx

    def max_sum3(self) -> int:
        # Print the sub array index also
        mx: int = -1234567
        sum: int = 0
        start_index: int = 0
        end_index: int = 0
        for i in range(len(self.arr)):
            if sum == 0:
                start_index = i
            sum += self.arr[i]
            if sum > mx:
                mx = sum
                end_index = i

            if sum < 0:
                sum = 0

        print(f"start index = {start_index}, end index = {end_index}")

        mx = max(mx, 0)
        return mx

    def print_arr(self):
        print(self.arr)


if __name__ == "__main__":
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    solution = Solution(arr)
    solution.print_arr()
    print(solution.max_sum3())
