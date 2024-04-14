"""Best time to buy sell stock to maximize profit."""

from typing import List


class Solution:
    # Function to find the maximum profit from buying and selling stocks
    def __max_profit(self, prices: List[int], n: int) -> int:
        max_profit: int = 0
        l, r = 0, 1  # Initialize two pointers for buying and selling days
        # Iterate through the prices array
        while r < n:
            # If the price on the selling day is greater than the buying day
            if prices[l] < prices[r]:
                # Calculate the profit by selling on the current day
                profit: int = prices[r] - prices[l]
                # Update the maximum profit if the current profit is greater
                max_profit = max(max_profit, profit)
            else:
                # If the price on the selling day is not greater, update the buying day
                l = r
            # Move to the next day
            r += 1

        return max_profit

    # Main function to find the maximum profit
    def maxProfit(self, prices: list[int]) -> int:
        n: int = len(prices)
        # Call the helper function to find the maximum profit
        return self.__max_profit(prices=prices, n=n)


# Test the maxProfit function
if __name__ == "__main__":
    prices: List[int] = [7, 1, 5, 3, 6, 4]
    solution: Solution = Solution()
    print(solution.maxProfit(prices=prices))
