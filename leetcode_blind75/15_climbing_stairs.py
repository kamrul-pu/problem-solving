class Solution:
    def __init__(self):
        self.dp = [-1] * 45

    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one

    def climbStairs1(self, n: int) -> int:
        if self.dp[n] != -1:
            return self.dp[n]
        if n < 0:
            return 0
        if n == 0:
            return 1
        self.dp[n] = self.climbStairs1(n - 1) + self.climbStairs1(n - 2)
        return self.dp[n]


if __name__ == "__main__":
    solution = Solution()
    n = 3
    print(solution.climbStairs(n))
    # print(solution.climbStairs1(n))
