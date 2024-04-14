"""Decode ways."""

from typing import List


class Solution:
    def __f(self, i: int, n: int, s: str, dp: List[int]) -> int:
        """
        Recursive function to count the number of ways to decode the string starting from index 'i'.

        Args:
            i (int): The starting index for decoding.
            n (int): The length of the string 's'.
            s (str): The input string to decode.
            dp (List[int]): Memoization table to store the results of subproblems.

        Returns:
            int: The number of ways to decode the string starting from index 'i'.
        """
        if i < n and s[i] == "0":
            return 0
        if i >= n - 1:
            return 1
        if dp[i] != -1:
            return dp[i]
        ans: int = self.__f(i + 1, n, s, dp)
        if i + 2 <= n and int(s[i : i + 2]) <= 26:
            ans += self.__f(i + 2, n, s, dp)
        dp[i] = ans
        return ans

    def __ways(self, s: str, n: int) -> int:
        """
        Function to count the number of ways to decode the string using memoization.

        Args:
            s (str): The input string to decode.
            n (int): The length of the string 's'.

        Returns:
            int: The number of ways to decode the string.
        """
        dp: List[int] = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1
        for i in range(2, n + 1):
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]
            if s[i - 2] != "0" and int(s[i - 2 : i]) <= 26:
                dp[i] += dp[i - 2]

        return dp[n]

    def __ways_optimal(self, s: str, n: int) -> int:
        """
        Function to count the number of ways to decode the string using an optimal approach.

        Args:
            s (str): The input string to decode.
            n (int): The length of the string 's'.

        Returns:
            int: The number of ways to decode the string.
        """
        two_back: int = 1
        one_back: int = 0 if s[0] == "0" else 1
        if n == 1:
            return one_back
        for i in range(2, n + 1):
            cur: int = 0
            if s[i - 1] != "0":
                cur += one_back
            if s[i - 2] != "0" and int(s[i - 2 : i]) <= 26:
                cur += two_back

            two_back = one_back
            one_back = cur
        return one_back

    def numDecodings(self, s: str) -> int:
        """
        Function to count the number of ways to decode the string.

        Args:
            s (str): The input string to decode.

        Returns:
            int: The number of ways to decode the string.
        """
        n: int = len(s)
        # Uncomment one of the following methods to use
        # dp: List[int] = [-1] * n
        # return self.__f(0, n, s, dp)  # Using recursion with memoization
        # return self.__ways(s=s, n=n)  # Using memoization
        return self.__ways_optimal(s=s, n=n)  # Using an optimal approach


if __name__ == "__main__":
    s: str = "226"
    solution: Solution = Solution()
    print(solution.numDecodings(s=s))
