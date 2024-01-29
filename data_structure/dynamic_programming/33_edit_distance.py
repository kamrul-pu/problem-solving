"""Edit distance. Recrusion 1D array Optimized solution."""


class Solution:
    def __f(self, i: int, j: int, word1: str, word2: str, dp: list[list[int]]) -> int:
        # Base cases
        if i == 0:
            return j
        if j == 0:
            return i
        if dp[i][j] != -1:
            return dp[i][j]

        # If the characters are the same, no operation is needed
        if word1[i - 1] == word2[j - 1]:
            return 0 + self.__f(i - 1, j - 1, word1, word2, dp)

        # Calculate costs for insert, delete, and replace operations
        insert: int = self.__f(i, j - 1, word1, word2, dp)
        delete: int = self.__f(i - 1, j, word1, word2, dp)
        replace: int = self.__f(i - 1, j - 1, word1, word2, dp)

        # Store the result in the dp table and return the calculated value
        dp[i][j] = 1 + min(insert, delete, replace)
        return dp[i][j]

    def minDistance(self, word1: str, word2: str) -> int:
        n: int = len(word1)
        m: int = len(word2)
        # Initialize a dp table with -1 values
        dp: list[list[int]] = [[-1 for col in range(m + 1)] for row in range(n + 1)]
        return self.__f(n, m, word1, word2, dp)

    def min_distance_tabulation(self, word1: str, word2: str) -> int:
        n: int = len(word1)
        m: int = len(word2)
        # Initialize a dp table with base cases
        dp: list[list[int]] = [[0 for col in range(m + 1)] for row in range(n + 1)]

        # Fill in the dp table using a bottom-up approach
        for j in range(m + 1):
            dp[0][j] = j
        for i in range(n + 1):
            dp[i][0] = i
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = 0 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

        return dp[n][m]

    def min_distance_optimal(self, word1: str, word2: str) -> int:
        n: int = len(word1)
        m: int = len(word2)
        # Initialize two arrays to represent the current and previous rows in the dp table
        prev: list[int] = [col for col in range(m + 1)]
        cur: list[int] = [col for col in range(m + 1)]

        # Fill in the dp table using an optimized space approach
        for i in range(1, n + 1):
            cur[0] = i
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    cur[j] = 0 + prev[j - 1]
                else:
                    cur[j] = 1 + min(cur[j - 1], prev[j], prev[j - 1])

            # Update the previous row with the current row for the next iteration
            prev = cur.copy()

        return prev[m]


if __name__ == "__main__":
    word1: str = "horse"
    word2: str = "ros"
    solution: Solution = Solution()
    # Test the three different methods for calculating edit distance
    print(solution.minDistance(word1, word2))
    print(solution.min_distance_tabulation(word1, word2))
    print(solution.min_distance_optimal(word1, word2))
