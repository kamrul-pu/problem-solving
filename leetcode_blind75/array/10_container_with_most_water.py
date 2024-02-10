"""Container with most water."""

from typing import List


class Solution:
    # Function to calculate the maximum area of water that can be trapped between the vertical lines
    def __f(self, height: List[int], n: int) -> int:
        ans: int = 0  # Initialize the maximum area to 0
        l: int = 0  # Initialize the left pointer to the first element
        h: int = n - 1  # Initialize the right pointer to the last element
        while l < h:  # Iterate until the left pointer is less than the right pointer
            # Calculate the area between the vertical lines at the current positions of the pointers
            area: int = (h - l) * min(height[l], height[h])
            ans = max(
                ans, area
            )  # Update the maximum area if the current area is greater
            # Move the pointer pointing to the shorter line towards the other pointer
            if height[l] < height[h]:
                l += 1
            else:
                h -= 1

        return ans  # Return the maximum area

    # Main function to find the maximum area of water that can be trapped
    def maxArea(self, height: list[int]) -> int:
        n: int = len(height)  # Get the length of the input list
        return self.__f(
            height=height, n=n
        )  # Call the helper function to calculate the maximum area


# Main function to test the maxArea function
if __name__ == "__main__":
    height: List[int] = [1, 8, 6, 2, 5, 4, 8, 3, 7]  # Example input heights
    solution: Solution = Solution()  # Create an instance of the Solution class
    print(
        solution.maxArea(height=height)
    )  # Print the maximum area of water that can be trapped
