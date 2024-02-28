"""
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix.
If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the
bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e.,
they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path."""

from collections import deque
from typing import Deque, List


class Solution:
    def __f(self, grid: List[List[int]], n: int) -> int:
        # Check if the starting cell is blocked
        if grid[0][0] == 1:
            return -1

        # Initialize distances matrix with infinity for all cells
        distances: List[List[int]] = [[float("inf")] * n for _ in range(n)]

        # Initialize a deque for BFS
        q: Deque = deque()
        distances[0][0] = 1  # Distance from start to start is 1
        q.append((1, 0, 0))  # Tuple: (distance, row, column) of the current cell

        # Perform BFS
        while q:
            distance, row, col = q.popleft()

            # Explore all 8 adjacent cells
            for i in range(-1, 2):
                for j in range(-1, 2):
                    n_row: int = row + i
                    n_col: int = col + j

                    # Check if the neighbor cell is within bounds and not blocked
                    if n > n_row >= 0 and n > n_col >= 0 and grid[n_row][n_col] == 0:
                        new_distance: int = distance + 1

                        # Update distance if it's smaller than the recorded distance
                        if new_distance < distances[n_row][n_col]:
                            distances[n_row][n_col] = new_distance

                            # If we reached the bottom-right cell, return the distance
                            if n_row == n - 1 and n_col == n - 1:
                                return new_distance

                            # Add the neighbor cell to the queue for further exploration
                            q.append((new_distance, n_row, n_col))

        # If we couldn't reach the bottom-right cell, return -1
        return (
            -1 if distances[n - 1][n - 1] == float("inf") else distances[n - 1][n - 1]
        )

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Get the size of the grid
        n: int = len(grid)

        # Call the private function to compute the shortest path
        return self.__f(grid=grid, n=n)


if __name__ == "__main__":
    # Example grid
    grid: List[List[int]] = [
        [0, 0, 0],
        [1, 1, 0],
        [1, 1, 0],
    ]

    # Create an instance of the Solution class
    solution: Solution = Solution()

    # Print the shortest path length
    print(solution.shortestPathBinaryMatrix(grid=grid))
