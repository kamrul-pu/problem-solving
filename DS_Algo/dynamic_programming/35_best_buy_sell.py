"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

from typing import List


class Solution:
    # This method is intended to find the maximum profit from stock prices.
    def __max(self, prices: List[int]) -> int:
        # Initialize mini to the first price and profit to 0.
        mini: int = prices[0]
        profit: int = 0

        # Loop through the prices starting from the second day.
        for i in range(1, len(prices)):
            # Calculate the potential profit if we sold on this day.
            cost: int = prices[i] - mini

            # Update profit if the calculated cost is greater than the current profit.
            profit = max(profit, cost)

            # Update mini to be the lowest price encountered so far.
            mini = min(mini, prices[i])

        # Return the maximum profit found.
        return profit

    # This method is a secondary approach to calculate max profit.
    def __f(self, prices: List[int], n: int) -> int:
        # Initialize max_profit to 0.
        max_profit: int = 0
        l, r = 0, 1  # l is the buy index, r is the sell index.

        # Loop until the right pointer reaches the end of the price list.
        while r < n:
            # If the current buy price is less than the sell price
            if prices[l] < prices[r]:
                # Calculate the profit from this transaction.
                profit: int = prices[r] - prices[l]
                # Update max_profit if the current profit is greater.
                max_profit = max(max_profit, profit)
            else:
                # If not, move the buy index to the sell index.
                l = r
            # Move the sell index to the next day.
            r += 1

        # Return the maximum profit found.
        return max_profit

    # This is the main method to be called to get the max profit.
    def maxProfit(self, prices: list[int]) -> int:
        n: int = len(prices)  # Get the length of the prices list.
        # Call the secondary method to compute max profit.
        return self.__f(prices=prices, n=n)


if __name__ == "__main__":
    # Example list of stock prices over days.
    prices: List[int] = [7, 1, 5, 3, 6, 4]
    # Create an instance of the Solution class.
    solution: Solution = Solution()
    # Print the maximum profit that can be achieved.
    print(solution.maxProfit(prices=prices))
