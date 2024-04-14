"""Jump game 2."""

from typing import List


class Solution:
    def __jumps(self, nums: List[int], n: int) -> int:
        """
        Function to calculate the minimum number of jumps required to reach the last index.

        Args:
            nums (List[int]): Integer array representing maximum jump length at each position.
            n (int): Length of the array.

        Returns:
            int: Minimum number of jumps required to reach the last index.
        """
        ans: int = 0  # Variable to store the minimum number of jumps
        l: int = 0  # Left boundary of the current jump
        r: int = 0  # Right boundary of the current jump
        while r < n - 1:
            farthest: int = (
                0  # Variable to store the farthest reachable index from the current jump
            )
            # Iterate through each index within the current jump boundaries
            for i in range(l, r + 1):
                farthest = max(
                    farthest, i + nums[i]
                )  # Update the farthest reachable index
            l = (
                r + 1
            )  # Move the left boundary of the next jump to the right boundary of the current jump
            r = farthest  # Update the right boundary of the next jump to the farthest reachable index
            ans += 1  # Increment the minimum number of jumps
        return ans  # Return the minimum number of jumps

    def jump(self, nums: List[int]) -> int:
        """
        Main function to determine the minimum number of jumps required to reach the last index.

        Args:
            nums (List[int]): Integer array representing maximum jump length at each position.

        Returns:
            int: Minimum number of jumps required to reach the last index.
        """
        n: int = len(nums)  # Length of the input array
        return self.__jumps(
            nums=nums, n=n
        )  # Call the helper function to calculate the minimum number of jumps


if __name__ == "__main__":
    nums: List[int] = [2, 3, 1, 1, 4]  # Example input array
    # nums = [2, 0, 0]  # Example input array
    # nums = [2, 3, 0, 1, 4]  # Example input array
    # nums = [1, 2, 3]  # Example input array
    solution: Solution = Solution()  # Create an instance of the Solution class
    print(
        solution.jump(nums=nums)
    )  # Print the minimum number of jumps required to reach the last index
