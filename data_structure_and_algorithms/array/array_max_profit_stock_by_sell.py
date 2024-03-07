"""Majority elements means a number appered more then n/2 times."""


class Solution:
    def __init__(self, arr) -> None:
        self.arr = arr

    def max_profit(self) -> int:
        profit = 0
        buy = self.arr[0]
        for i in range(1, len(self.arr)):
            cost = self.arr[i] - buy
            profit = max(profit, cost)
            buy = min(buy, self.arr[i])

        return profit

    def max_profit_buy_sell_day(self) -> dict:
        profit = 0
        buy = self.arr[0]
        buy_day = sell_day = 0
        for i in range(1, len(self.arr)):
            cost = self.arr[i] - buy
            if cost > profit:
                profit = cost
                sell_day = i

            if self.arr[i] < buy:
                buy = self.arr[i]
                buy_day = i

        return {
            "buy": buy_day + 1,
            "sell": sell_day + 1,
            "profit": profit,
        }

    def print_arr(self):
        print(self.arr)


if __name__ == "__main__":
    arr = [7, 1, 5, 3, 6, 4]
    solution = Solution(arr)
    solution.print_arr()
    print(solution.max_profit())
    print(solution.max_profit_buy_sell_day())
