"""
Given an array of integers heights representing the histogram's bar height where
the width of each bar is 1, return the area of the largest rectangle in the histogram.
"""

from typing import List, Tuple


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Get the length of the heights array
        n: int = len(heights)

        # Initialize a variable to store the maximum area of the rectangle
        mx_area: int = 0

        # Stack to keep track of indices and corresponding heights
        stack: List[Tuple[int, int]] = []  # (index, height)

        # Iterate through each bar in the histogram
        for i, h in enumerate(heights):
            start = i

            # Process the stack while it's not empty and the top bar's height is greater than the current bar's height
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                # Calculate the area using the popped bar's height and width (distance to current bar)
                mx_area = max(mx_area, height * (i - index))
                # Update the start index to the popped bar's index
                start = index

            # Push the current bar's start index and height to the stack
            stack.append((start, h))

        # After processing all bars, check if there are any bars left in the stack
        # They represent bars with increasing heights till the end of the histogram
        for index, height in stack:
            # Calculate the area using the remaining bars in the stack
            mx_area = max(mx_area, height * (n - index))

        # Return the maximum area of the largest rectangle
        return mx_area


if __name__ == "__main__":
    heights: List[int] = [2, 1, 5, 6, 2, 3]
    solution: Solution = Solution()
    print(solution.largestRectangleArea(heights=heights))

    print("Program finished!!!")
