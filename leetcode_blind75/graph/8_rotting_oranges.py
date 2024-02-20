"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1
"""

from collections import deque
from typing import Deque, List, Tuple


class Solution:
    def __f(self, grid: List[List[int]], n: int, m: int) -> int:
        # Initialize a 2D array to keep track of visited cells
        visited: List[List[bool]] = [[False] * m for _ in range(n)]

        # Initialize a deque to perform BFS
        q: Deque = deque()

        # Count the number of fresh oranges
        cnt_fresh: int = 0

        # Iterate through the grid to populate the deque and count fresh oranges
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    # Add the coordinates of rotten oranges to the deque
                    q.append((i, j, 0))  # Tuple format: (row, column, time)
                    # Mark the current cell as visited
                    visited[i][j] = True
                elif grid[i][j] == 1:
                    # Count the number of fresh oranges
                    cnt_fresh += 1

        # Initialize variables to keep track of rotten oranges and time taken
        rotten: int = 0
        tm: int = 0

        # Define deltas for moving in four directions (up, right, down, left)
        del_row: List[int] = [-1, 0, 1, 0]
        del_col: List[int] = [0, 1, 0, -1]

        # Perform BFS until the deque is empty
        while q:
            # Pop the front element of the deque
            front: Tuple = q.popleft()
            r, c, t = front
            # Update time taken
            tm = max(tm, t)

            # Explore neighbors of the current cell
            for i in range(4):
                nrow: int = r + del_row[i]
                ncol: int = c + del_col[i]

                # Check if the neighbor is within grid boundaries, not visited, and a fresh orange
                if (
                    n > nrow >= 0
                    and m > ncol >= 0
                    and not visited[nrow][ncol]
                    and grid[nrow][ncol] == 1
                ):
                    # Add the neighbor to the deque
                    q.append((nrow, ncol, t + 1))
                    # Mark the neighbor as visited
                    visited[nrow][ncol] = True
                    # Increment the count of rotten oranges
                    rotten += 1

        # If the count of rotten oranges is not equal to the count of fresh oranges, return -1
        return -1 if rotten != cnt_fresh else tm

    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Get the dimensions of the grid
        n: int = len(grid)
        m: int = len(grid[0])
        # Call the helper function to find the minimum number of minutes
        return self.__f(grid=grid, n=n, m=m)


# Test the solution
if __name__ == "__main__":
    # Example grid
    grid: List[List[int]] = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    # Create an instance of the solution class
    solution: Solution = Solution()
    # Print the minimum number of minutes required
    print(solution.orangesRotting(grid=grid))
