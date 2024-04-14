"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
"""

from collections import deque
from typing import Deque, List, Tuple


class Solution:
    def __f(self, mat: List[List[int]], n: int, m: int) -> List[List[int]]:
        # Initialize a 2D list to keep track of visited cells
        visited: List[List[int]] = [[False] * m for _ in range(n)]

        # Initialize a 2D list to store distances from each cell to the nearest 0
        distances: List[List[int]] = [[0] * m for _ in range(n)]

        # Initialize a deque for BFS traversal
        q: Deque = deque()

        # Iterate through the matrix to find cells with value 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    # Add the coordinates of cells with value 0 to the deque
                    q.append((i, j, 0))
                    # Mark the cell as visited
                    visited[i][j] = True

        # Define deltas for moving in four directions (up, right, down, left)
        del_row: List[int] = [-1, 0, 1, 0]
        del_col: List[int] = [0, 1, 0, -1]

        # Perform BFS traversal
        while q:
            front: Tuple = q.popleft()
            row, col, distance = front
            distances[row][col] = distance  # Store the distance in the distances matrix

            # Explore neighbors of the current cell
            for i in range(4):
                nrow: int = row + del_row[i]
                ncol: int = col + del_col[i]
                # Check if the neighbor is within grid boundaries and not visited
                if n > nrow >= 0 and m > ncol >= 0 and not visited[nrow][ncol]:
                    # Add the neighbor to the deque
                    q.append((nrow, ncol, distance + 1))
                    # Mark the neighbor as visited
                    visited[nrow][ncol] = True

        return distances

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # get the length of the matrix
        n: int = len(mat)  # number of rows
        m: int = len(mat[0])  # number of columns
        # call the helper method to calculate the distance
        return self.__f(mat=mat, n=n, m=m)


# Test the solution
if __name__ == "__main__":
    # Example matrix
    mat: List[List[int]] = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    # Create an instance of the solution class
    solution: Solution = Solution()
    # Print the updated matrix with distances to nearest 0
    print(solution.updateMatrix(mat=mat))
