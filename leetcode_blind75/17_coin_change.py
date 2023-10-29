dp = [-1] * 10000


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount] if dp[amount] != amount + 1 else -1

    def coin_change1(self, coins: list[int], amount: int) -> int:
        if dp[amount] != -1:
            return dp[amount]
        if amount == 0:
            return 0
        ans = 1e3 + 10
        for coin in coins:
            if amount - coin >= 0:
                dp[amount] = min(ans, self.coin_change1(coins, amount - coin) + 1)
        return dp[amount]


def coin_change(coins, amount) -> int:
    if amount == 0:
        return 0
    ans = 1e5 + 10
    for coin in coins:
        if amount - coin >= 0:
            ans = min(ans, coin_change(coins, amount - coin) + 1)

    return ans


if __name__ == "__main__":
    solution = Solution()
    coins = [1, 2, 5]
    amount = 40
    # print(coin_change(coins, amount))
    # print(solution.coinChange(coins, amount))
    # print(solution.climbStairs1(n))
    print(solution.coin_change1(coins, amount))
