"""
You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another
4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can
swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).
"""

import heapq
from typing import List, Tuple


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Get the size of the grid
        n: int = len(grid)

        # Initialize a boolean matrix to keep track of visited cells
        visited: List[List[bool]] = [[False] * n for _ in range(n)]

        # Initialize a priority queue to store cells in the order of time/max-height
        # The priority queue will store tuples of (time, row, col)
        pq: List[Tuple[int]] = [(grid[0][0], 0, 0)]

        # Define directions to move (up, down, left, right)
        directions: List[List[int]] = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # Mark the starting cell as visited
        visited[0][0] = True

        # Iterate while there are cells in the priority queue
        while pq:
            # Pop the cell with the minimum time/max-height from the priority queue
            front: Tuple[int] = heapq.heappop(pq)
            time, row, col = front

            # Check if we've reached the bottom right cell
            if row == n - 1 and col == n - 1:
                return time

            # Explore all four directions from the current cell
            for dr, dc in directions:
                n_row: int = row + dr
                n_col: int = col + dc

                # Check if the next cell is out of bounds or already visited
                if (
                    n_row < 0
                    or n_col < 0
                    or n_row == n
                    or n_col == n
                    or visited[n_row][n_col]
                ):
                    continue

                # Mark the next cell as visited
                visited[n_row][n_col] = True

                # Push the next cell to the priority queue with its updated time/max-height
                heapq.heappush(pq, (max(time, grid[n_row][n_col]), n_row, n_col))


if __name__ == "__main__":
    grid: List[List[int]] = [
        [0, 1, 2, 3, 4],
        [24, 23, 22, 21, 5],
        [12, 13, 14, 15, 16],
        [11, 17, 18, 19, 20],
        [10, 9, 8, 7, 6],
    ]
    solution: Solution = Solution()
    print(solution.swimInWater(grid=grid))
