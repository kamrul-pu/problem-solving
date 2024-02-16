"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].
To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color 
as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color
of all of the aforementioned pixels with color.
Return the modified image after performing the flood fill.
"""

from typing import List


class Solution:
    def __dfs(
        self,
        sr: int,
        sc: int,
        image: List[List[int]],
        init_color: int,
        new_color: int,
        ans: List[List[int]],
    ) -> None:
        # Mark the current cell with the new color
        ans[sr][sc] = new_color
        # Get the number of rows and columns in the image
        n: int = len(image)
        m: int = len(image[0])
        # Define the directions to explore (up, right, down, left)
        del_row: List[int] = [-1, 0, 1, 0]
        del_col: List[int] = [0, 1, 0, -1]
        # Explore neighbors in four directions (up, right, down, left)
        for i in range(4):
            nrow: int = sr + del_row[i]
            ncol: int = sc + del_col[i]
            # Check if the neighbor is within the bounds of the image
            # and has the same initial color, and hasn't been visited yet
            if (
                n > nrow >= 0
                and m > ncol >= 0
                and image[nrow][ncol] == init_color
                and image[nrow][ncol] != new_color
            ):
                # Recursive call to explore the neighbor
                self.__dfs(nrow, ncol, image, init_color, new_color, ans)

    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        # Get the initial color of the starting point
        init_color: int = image[sr][sc]

        # Create a copy of the image to store the result
        ans: list[list[int]] = image.copy()
        # Call the DFS function to perform flood fill
        self.__dfs(sr, sc, image, init_color, color, ans)

        # Return the updated image after flood fill
        return ans


if __name__ == "__main__":
    # Example usage of the flood_fill function
    image: List[List[int]] = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr: int = 1
    sc: int = 1
    color: int = 2
    solution: Solution = Solution()
    # Perform flood fill starting from position (1, 1) with new color 2
    print(solution.floodFill(image=image, sr=sr, sc=sc, color=color))
