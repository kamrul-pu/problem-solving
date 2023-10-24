"""
Buy Sell Profit Porblem solution.
Complexity: Time O(1)
            Space O(n)
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        # Left is buy Right = sell
        l, r = 0, 1  # Left and right pointer is initialized as 0 and 1
        while r < len(prices):
            # profitable transaction ?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            r += 1

        return max_profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    solution = Solution()
    print(solution.maxProfit(prices=prices))
    prices = [7, 6, 4, 3, 1]
    print(solution.maxProfit(prices=prices))
