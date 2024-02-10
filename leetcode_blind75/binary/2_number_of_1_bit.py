"""Number of 1 bits."""


class Solution:
    def hammingWeight(self, n: int) -> int:
        ans: int = 0
        while n:
            ans += n & 1
            n >>= 1
        return ans


if __name__ == "__main__":
    n: int = 11
    solution: Solution = Solution()
    print(solution.hammingWeight(n=n))
