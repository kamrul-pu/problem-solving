"""Leaders mean the all right most element should be smaller."""


class Solution:
    def __init__(self, arr: list[int]) -> None:
        self.arr = arr

    def longest_consequtive_seqence(self) -> int:
        # sort the array
        self.arr.sort()
        longest: int = 1
        last_smaller: int = -12435436
        count: int = 0
        for i in range(len(self.arr)):
            if self.arr[i] - 1 == last_smaller:
                count += 1
                last_smaller = self.arr[i]
            elif self.arr[i] != last_smaller:
                count = 1
                last_smaller = self.arr[i]
            longest = max(longest, count)

        return longest

    def print_arr(self) -> None:
        print(self.arr)


if __name__ == "__main__":
    arr = [102, 4, 100, 1, 101, 3, 2, 1, 1]
    solution = Solution(arr)
    solution.print_arr()
    print(solution.longest_consequtive_seqence())
    solution.print_arr()
