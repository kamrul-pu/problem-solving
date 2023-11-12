"""Number of available subarray with the given xor k"""


class Solution:
    def __init__(self, arr: list[list[int]]) -> None:
        self.arr = arr

    def merge_overlaping_intervals_brute_force(self) -> list[list[int]]:
        n = len(self.arr)
        self.arr.sort()
        ans: list[list[int]] = []
        for i in range(n):
            start: int = self.arr[i][0]
            end: int = self.arr[i][1]
            if len(ans) != 0 and end <= ans[-1][1]:
                continue

            for j in range(i + 1, n):
                if self.arr[j][0] <= end:
                    end = max(self.arr[j][1], end)
                else:
                    break
            ans.append([start, end])

        return ans

    def merge_overlapping_intervals_optimal(self) -> list[list[int]]:
        # Declare a list for storing result
        ans: list[list[int]] = []
        # take the size of the array
        n = len(self.arr)
        # sort the array
        self.arr.sort()

        # for i in range(n):
        #     if len(ans) == 0:
        #         ans.append([self.arr[i][0], self.arr[i][1]])
        #         continue
        #     start: int = self.arr[i][0]
        #     end: int = self.arr[i][1]
        #     if len(ans) != 0 and start <= ans[-1][1]:
        #         ans[-1][1] = max(end, ans[-1][1])
        #     else:
        #         ans.append([start, end])

        ans.append([self.arr[0][0], self.arr[0][1]])
        for i in range(1, n):
            start: int = self.arr[i][0]
            end: int = self.arr[i][1]

            if start <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], end)
            else:
                ans.append([self.arr[i][0], self.arr[i][1]])
        return ans

    def print_arr(self) -> None:
        print(self.arr, sep=" ")
        print()


if __name__ == "__main__":
    arr = [[1, 3], [2, 6], [8, 9], [9, 11], [8, 10], [2, 4], [15, 18], [16, 17]]
    solution = Solution(arr)
    solution.print_arr()
    print(solution.merge_overlaping_intervals_brute_force())
    print(solution.merge_overlapping_intervals_optimal())
