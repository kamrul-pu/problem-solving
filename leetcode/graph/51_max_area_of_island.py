"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally
(horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
"""

from collections import deque
from typing import List, Deque, Tuple


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Get the number of rows and columns in the grid
        n: int = len(grid)
        m: int = len(grid[0])
        # Initialize a 2D array to keep track of visited cells
        visited: List[List[bool]] = [[False for col in range(m)] for _ in range(n)]
        # Initialize the maximum area of an island
        mx_area: int = 0

        # Define a BFS function to traverse the island
        def bfs(r: int, c: int) -> int:
            # Initialize the count of cells in the island
            cnt: int = 0
            # Initialize a queue for BFS traversal
            q: Deque[Tuple[int]] = deque()
            # Add the starting cell to the queue and mark it as visited
            q.append((r, c))
            visited[r][c] = True
            # Define directions for movement: up, right, down, left
            dr: List[int] = [-1, 0, 1, 0]
            dc: List[int] = [0, 1, 0, -1]
            # Traverse the island using BFS
            while q:
                # Pop the cell from the queue
                row, col = q.popleft()
                # Increment the count of cells in the island
                cnt += 1
                # Explore neighboring cells in all four directions
                for i in range(len(dr)):
                    nrow: int = dr[i] + row
                    ncol: int = dc[i] + col
                    # Check if the neighboring cell is within the grid and is part of the island
                    if (
                        nrow >= 0
                        and ncol >= 0
                        and nrow < n
                        and ncol < m
                        and grid[nrow][ncol] == 1
                        and not visited[nrow][ncol]
                    ):
                        # Add the neighboring cell to the queue and mark it as visited
                        q.append((nrow, ncol))
                        visited[nrow][ncol] = True
            # Return the count of cells in the island
            return cnt

        # Iterate through each cell in the grid
        for r in range(n):
            for c in range(m):
                # If the cell represents land and has not been visited yet
                if grid[r][c] == 1 and not visited[r][c]:
                    # Calculate the area of the island starting from this cell using BFS
                    mx_area = max(mx_area, bfs(r, c))
        # Return the maximum area of an island
        return mx_area


if __name__ == "__main__":
    # Example grid representing the map with 1's as land and 0's as water
    grid: List[List[int]] = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]
    # Create an instance of the Solution class
    solution: Solution = Solution()
    # Call the maxAreaOfIsland function with the example grid and print the result
    print(solution.maxAreaOfIsland(grid=grid))
