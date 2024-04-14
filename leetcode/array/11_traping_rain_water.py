"""Trapping rain water."""

from typing import List


class Solution:
    def __brute_force(self, height: List[int], n: int) -> int:
        """
        Brute force method to calculate the amount of trapped rainwater.

        Args:
            height (List[int]): List of heights of walls.
            n (int): Number of elements in the height list.

        Returns:
            int: Amount of trapped rainwater.
        """
        prefix: List[int] = [
            0
        ] * n  # List to store maximum height from the left for each element
        sufix: List[int] = [
            0
        ] * n  # List to store maximum height from the right for each element
        p_max: int = 0  # Maximum height encountered from the left
        s_max: int = 0  # Maximum height encountered from the right
        for i in range(n):
            p_max = max(p_max, height[i])  # Update p_max
            s_max = max(s_max, height[n - i - 1])  # Update s_max
            prefix[i] = (
                p_max  # Store maximum height from the left for the current element
            )
            sufix[n - i - 1] = (
                s_max  # Store maximum height from the right for the current element
            )

        ans: int = 0  # Initialize the amount of trapped rainwater
        for i in range(n):
            ans += (
                min(prefix[i], sufix[i]) - height[i]
            )  # Calculate trapped rainwater for each element

        return ans  # Return the total amount of trapped rainwater

    def __trap_water(self, height: List[int], n: int) -> int:
        """
        Efficient method to calculate the amount of trapped rainwater using two pointers.

        Args:
            height (List[int]): List of heights of walls.
            n (int): Number of elements in the height list.

        Returns:
            int: Amount of trapped rainwater.
        """
        l: int = 0  # Left pointer
        r: int = n - 1  # Right pointer
        left_max: int = 0  # Maximum height encountered from the left
        right_max: int = 0  # Maximum height encountered from the right
        ans: int = 0  # Initialize the amount of trapped rainwater

        while l <= r:
            if height[l] <= height[r]:
                if height[l] >= left_max:
                    left_max = height[l]  # Update left_max
                else:
                    ans += (
                        left_max - height[l]
                    )  # Calculate trapped rainwater for the current position
                l += 1  # Move the left pointer

            else:
                if height[r] >= right_max:
                    right_max = height[r]  # Update right_max
                else:
                    ans += (
                        right_max - height[r]
                    )  # Calculate trapped rainwater for the current position
                r -= 1  # Move the right pointer

        return ans  # Return the total amount of trapped rainwater

    def trap(self, height: List[int]) -> int:
        """
        Main function to calculate the amount of trapped rainwater.

        Args:
            height (List[int]): List of heights of walls.

        Returns:
            int: Amount of trapped rainwater.
        """
        n: int = len(height)  # Get the number of elements in the height list
        # return self.__brute_force(height=height, n=n)  # Use brute force method
        return self.__trap_water(
            height=height, n=n
        )  # Use efficient two pointers method


if __name__ == "__main__":
    # Example input list of heights
    height: List[int] = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    solution: Solution = Solution()  # Create an instance of the Solution class
    print(solution.trap(height=height))  # Print the amount of trapped rainwater
