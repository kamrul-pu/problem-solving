"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume 
all four edges of the grid are all surrounded by water.
"""

from typing import List, Deque, Tuple

from collections import deque


class Solution:
    def __bfs(
        self,
        i: int,
        j: int,
        n: int,
        m: int,
        grid: List[List[int]],
        visited: List[List[int]],
    ) -> None:
        # Mark the current cell as visited
        visited[i][j] = True
        # Initialize a deque for BFS traversal
        q: Deque = deque()
        q.append((i, j))
        # Define the direction vectors for navigating neighboring cells (up, right, down, left)
        di: List[int] = [-1, 0, 1, 0]
        dj: List[int] = [0, 1, 0, -1]

        while q:
            # Extract the front of the queue
            front: Tuple = q.popleft()
            row: int = front[0]
            col: int = front[1]
            # Explore all neighboring cells
            for k in range(len(di)):
                nrow: int = row + di[k]
                ncol: int = col + dj[k]
                # Check if the neighboring cell is within bounds and is land ("1") and has not been visited
                if (
                    n > nrow >= 0
                    and m > ncol >= 0
                    and grid[nrow][ncol] == "1"
                    and not visited[nrow][ncol]
                ):
                    # Mark the neighboring cell as visited and add it to the queue for further exploration
                    visited[nrow][ncol] = True
                    q.append((nrow, ncol))

    def numIslands(self, grid: List[List[str]]) -> int:
        # Get the dimensions of the grid
        n: int = len(grid)
        m: int = len(grid[0])
        # Initialize a 2D array to keep track of visited cells
        visited: List[List[bool]] = [[False for col in range(m)] for _ in range(n)]
        # Counter for the number of islands
        cnt: int = 0
        # Iterate through each cell in the grid
        for i in range(n):
            for j in range(m):
                # If the cell is land ("1") and has not been visited, start BFS traversal
                if not visited[i][j] and grid[i][j] == "1":
                    self.__bfs(i, j, n, m, grid, visited)
                    cnt += 1  # Increment the island count

        return cnt


if __name__ == "__main__":
    # Sample grid representing land ("1") and water ("0")
    grid: List[List[str]] = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    # Create an instance of the Solution class
    solution: Solution = Solution()
    # Call the numIslands method to count the number of islands in the grid and print the result
    print(solution.numIslands(grid=grid))
