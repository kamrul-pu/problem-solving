"""Evaluate Boolean Expression to True."""

from typing import List


class Solution:
    def __f(
        self, i: int, j: int, expression: str, is_true: int, dp: List[List[List[int]]]
    ) -> int:
        # Recursive function to evaluate the number of ways expression can be True
        if i > j:
            return 0
        if i == j:
            # Base case: if the expression contains only one character
            if is_true:
                return expression[i] == "T"  # If is_true, check if it's 'T', else 'F'
            return expression[i] == "F"  # If not is_true, check if it's 'F', else 'T'
        if dp[i][j][is_true] != -1:
            return dp[i][j][is_true]  # Return already calculated value
        ways: int = 0  # Initialize number of ways
        for ind in range(i + 1, j, 2):
            # Iterate through operators (&, |, ^) in the expression
            lt: int = self.__f(
                i, ind - 1, expression, 1, dp
            )  # Evaluate left side to True
            lf: int = self.__f(
                i, ind - 1, expression, 0, dp
            )  # Evaluate left side to False
            rt: int = self.__f(
                ind + 1, j, expression, 1, dp
            )  # Evaluate right side to True
            rf: int = self.__f(
                ind + 1, j, expression, 0, dp
            )  # Evaluate right side to False

            if expression[ind] == "&":
                # If current operator is '&'
                if is_true:
                    ways += rt * lt  # True only if both sides are True
                else:
                    ways += (
                        (rt * lf) + (rf * lt) + (rf * lf)
                    )  # False can be achieved by any combination
            elif expression[ind] == "|":
                # If current operator is '|'
                if is_true:
                    ways += (
                        (lt * rt) + (lt * rf) + (lf * rt)
                    )  # True can be achieved by any combination
                else:
                    ways += rf * lf  # False only if both sides are False
            else:
                # If current operator is '^' (XOR)
                if is_true:
                    ways += (lt * rf) + (
                        lf * rt
                    )  # True if one side is True and the other is False
                else:
                    ways += (lt * rt) + (lf * rf)  # False if both sides are same
        dp[i][j][is_true] = ways  # Store the number of ways in the DP table
        return ways

    def number_of_ways(self, expression: str) -> int:
        n: int = len(expression)
        dp: List[List[List[int]]] = [
            [[-1 for ic in range(2)] for col in range(n)] for row in range(n)
        ]  # Initialize DP table with -1
        return self.__f(
            0, n - 1, expression, 1, dp
        )  # Call recursive function with initial parameters


if __name__ == "__main__":
    expression: str = "TIT&F"  # Example expression
    solution: Solution = Solution()
    print(
        solution.number_of_ways(expression=expression)
    )  # Print the number of ways the expression can be True
