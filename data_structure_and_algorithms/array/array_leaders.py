"""Leaders mean the all right most element should be smaller."""


class Solution:
    def __init__(self, arr: list[int]) -> None:
        self.arr = arr

    def find_leaders1(self) -> list[int]:
        """Brute force solution.
        TC O(n^2) space O(n)
        """
        leaders = []
        n = len(self.arr)
        for i in range(n):
            leader: bool = True
            for j in range(i + 1, n):
                if self.arr[j] > arr[i]:
                    leader = False
                    break
            if leader:
                leaders.append(self.arr[i])
        return leaders

    def find_leaders2(self) -> list[int]:
        """Optimal soltion
        TC O(n) Space O(n)
        TC O(nlogn) if result will return as a list
        """
        leaders = []
        n = len(self.arr)
        mx = -1234567
        for i in range(n - 1, -1, -1):
            if self.arr[i] > mx:
                leaders.append(self.arr[i])
            mx = max(mx, self.arr[i])

        leaders.reverse()
        return leaders

    def print_arr(self):
        print(self.arr)


if __name__ == "__main__":
    arr = [10, 22, 12, 3, 0, 6]
    solution = Solution(arr)
    solution.print_arr()
    leaders = solution.find_leaders1()
    print(leaders)
    leaders = solution.find_leaders2()
    print(leaders)
