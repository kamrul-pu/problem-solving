import array


class Solution:
    def countBits(self, n: int) -> list[int]:
        result = [0] * (n + 1)
        for i in range(n + 1):
            result[i] = self.numberOfSetBits(i)

        return result

    def numberOfSetBits(self, num: int) -> int:
        count = 0
        while num:
            count += num & 1
            num >>= 1

        return count

    # Another solution using dynamic programming
    def countBits2(self, n: int) -> int:
        dp = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]

        return dp

    def countBits3(self, n: int) -> int:
        dp = array.array("i", [0] * (n + 1))
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp


if __name__ == "__main__":
    solution = Solution()
    n = 5
    print(solution.countBits3(n))
