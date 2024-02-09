"""Maximum rectangle area with all 1's."""

from typing import List


class Solution:
    # Function to calculate the largest rectangle area in a histogram
    def __largest_rectangle_area(self, heights: List[int]) -> int:
        n: int = len(heights)
        st: List[int] = []  # stack to store indices of heights
        leftsmall: List[int] = [
            0
        ] * n  # array to store the index of the nearest smaller element to the left
        rightsmall: List[int] = [
            0
        ] * n  # array to store the index of the nearest smaller element to the right

        # Finding the index of the nearest smaller element to the left for each element
        for i in range(n):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            leftsmall[i] = 0 if not st else st[-1] + 1
            st.append(i)

        st.clear()  # clear the stack to be re-used

        # Finding the index of the nearest smaller element to the right for each element
        for i in range(n - 1, -1, -1):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            rightsmall[i] = n - 1 if not st else st[-1] - 1
            st.append(i)

        # Calculating the maximum area rectangle
        maxA = 0
        for i in range(n):
            maxA = max(maxA, heights[i] * (rightsmall[i] - leftsmall[i] + 1))

        return maxA

    # Function to calculate the maximal rectangle in a binary matrix
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n: int = len(matrix)
        m: int = len(matrix[0])
        max_area: int = 0
        height: List[int] = [0] * m  # array to store the heights of the histogram

        # Iterating through each row of the matrix
        for i in range(n):
            # Updating the histogram based on the current row
            for j in range(m):
                if matrix[i][j] == "1":
                    height[j] += 1
                else:
                    height[j] = 0
            # Calculating the largest rectangle area for the histogram
            area: int = self.__largest_rectangle_area(height)
            max_area = max(area, max_area)

        return max_area


# Test the maximalRectangle function
if __name__ == "__main__":
    matrix: List[List[str]] = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]

    solution: Solution = Solution()
    print(solution.maximalRectangle(matrix=matrix))
