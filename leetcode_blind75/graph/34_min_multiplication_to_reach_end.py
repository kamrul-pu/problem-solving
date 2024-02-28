"""
Given start, end and an array arr of n numbers. At each step, start is multiplied with any number
in the array and then mod operation with100000 is done to get the new start.

Your task is to find the minimum steps in which end can be achieved starting from start.
If it is not possible to reach end, then return -1.
"""

from collections import deque
from typing import Deque, List

MOD: int = 100000


class Solution:
    def __f(self, arr: List[int], start: int, end: int) -> int:
        # Initialize an array to store distances to each possible number
        distance: List[int] = [float("inf")] * MOD
        distance[start] = 0  # Distance from start to start is 0

        # Initialize a deque for BFS
        q: Deque = deque()
        q.append((start, 0))  # Tuple: (current number, number of steps)

        # Perform BFS
        while q:
            node, steps = q.popleft()

            # Try multiplying current number with each number in the array
            for num in arr:
                number: int = (
                    num * node
                ) % MOD  # Perform modulo operation to avoid overflow

                # If we haven't visited this number with fewer steps, update the distance and add to queue
                if steps + 1 < distance[number]:
                    distance[number] = steps  # Update distance to this number
                    if number == end:
                        return (
                            steps + 1
                        )  # If we reach the end number, return the total steps
                    q.append(
                        (number, steps + 1)
                    )  # Add the number to the queue with increased steps

        return -1  # If end is not reachable, return -1

    def minimumMultiplications(self, arr: List[int], start: int, end: int) -> int:
        # Check if start is already the end number
        if start == end:
            return 0

        # Call the private function to compute the minimum steps
        return self.__f(arr=arr, start=start, end=end)


if __name__ == "__main__":
    arr: List[int] = [2, 5, 7]
    start: int = 3
    end: int = 30

    # Create an instance of the Solution class
    solution: Solution = Solution()

    # Print the minimum steps required to reach end from start using multiplications
    print(solution.minimumMultiplications(arr=arr, start=start, end=end))
