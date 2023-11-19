"""
Find nth root.
N = 3 M = 27 3sqrt(27) = 3  ans: 3X3X3 =27
N = 4 M = 69 4sqrt(69) = -1 
"""


class Solution:
    def find_nth_root(self, n: int, m: int) -> int:
        ans = -1
        for i in range(1, m + 1):
            temp: int = i**n
            if temp == m:
                return i
            if temp > m:
                break
        return ans

    def find_nth_root_bs(self, n: int, m: int) -> int:
        ans = -1
        low: int = 1
        high: int = m
        while low <= high:
            mid: int = (low + high) // 2
            tmp: int = mid**n
            if tmp == m:
                return mid
            if tmp > m:
                high = mid - 1
            else:
                low = mid + 1

        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.find_nth_root(n=3, m=27))
    print(solution.find_nth_root_bs(n=3, m=27))
    print(solution.find_nth_root(n=4, m=69))
    print(solution.find_nth_root_bs(n=4, m=69))
