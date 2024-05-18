"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean
touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where
heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west
if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
"""

from typing import List, Set, Tuple


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Extracting the dimensions of the island
        rows, cols = len(heights), len(heights[0])

        # Sets to store coordinates reachable from Pacific and Atlantic respectively
        pacific, atlantic = set(), set()

        # Depth First Search (DFS) function to traverse the island
        def dfs(r: int, c: int, visit: Set[Tuple[int]], prev_height: int):
            # Base cases to terminate recursion:
            # 1. If the cell has been visited already
            # 2. If the cell is out of bounds
            # 3. If the cell's height is lower than the previous cell's height
            if (
                (r, c) in visit
                or r < 0
                or c < 0
                or r == rows
                or c == cols
                or heights[r][c] < prev_height
            ):
                return
            # Mark the cell as visited
            visit.add((r, c))
            # Recursively call DFS on neighboring cells
            dfs(r + 1, c, visit, heights[r][c])  # Down
            dfs(r - 1, c, visit, heights[r][c])  # Up
            dfs(r, c + 1, visit, heights[r][c])  # Right
            dfs(r, c - 1, visit, heights[r][c])  # Left

        # Traversing the first and last rows to find cells reachable from Pacific and Atlantic
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])  # Traverse top row
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])  # Traverse bottom row

        # Traversing the first and last columns to find cells reachable from Pacific and Atlantic
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])  # Traverse leftmost column
            dfs(
                r, cols - 1, atlantic, heights[r][cols - 1]
            )  # Traverse rightmost column

        # Finding cells reachable from both Pacific and Atlantic
        result: List[List[int]] = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result


if __name__ == "__main__":
    heights: List[List[int]] = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
    solution: Solution = Solution()
    result: List[List[int]] = solution.pacificAtlantic(heights=heights)
    print(result)
