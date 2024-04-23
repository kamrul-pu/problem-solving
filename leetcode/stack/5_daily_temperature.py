"""
Given an array of integers temperatures represents the daily temperatures, return an array answer
such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.
"""

from typing import List, Tuple


class Solution:
    def __brute(self, temperatures: List[int]) -> List[int]:
        # Brute force approach: O(n^2) time complexity
        n: int = len(temperatures)
        if n == 1:
            return []
        ans: List[int] = [0] * n
        for i in range(n - 1):
            days: int = 1
            for j in range(i + 1, n):
                if temperatures[j] > temperatures[i]:
                    ans[i] = days
                    break
                days += 1
        return ans

    def __f(self, temperatures: List[int]) -> List[int]:
        # Optimized approach using a stack: O(n) time complexity
        result: List[int] = [0] * len(temperatures)
        stack: List[Tuple[int, int]] = []  # (temperature, index)

        for i, t in enumerate(temperatures):
            # While there are temperatures in the stack and the current temperature is higher than the last temperature in the stack
            while stack and t > stack[-1][0]:
                stack_temp, stack_ind = (
                    stack.pop()
                )  # Pop the last temperature and its index from the stack
                result[stack_ind] = (
                    i - stack_ind
                )  # Calculate the number of days to wait
            stack.append(
                (t, i)
            )  # Push the current temperature and its index to the stack

        return result

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Choose the optimized approach using a stack
        return self.__f(temperatures=temperatures)


if __name__ == "__main__":
    temperatures: List[int] = [73, 74, 75, 71, 69, 72, 76, 73]
    solution: Solution = Solution()
    print(solution.dailyTemperatures(temperatures=temperatures))
