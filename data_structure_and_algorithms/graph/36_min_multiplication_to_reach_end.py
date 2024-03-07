"""Minimum Multiplication to reach end."""

from collections import deque
from typing import Deque, List

# Define a constant for modulo operation
MOD: int = 100000


def find_min_step(arr: List[int], start: int, end: int) -> int:
    # Initialize a deque for BFS traversal
    q: Deque = deque()
    # Add the starting node and steps to the queue
    q.append((start, 0))

    # Initialize distance array with infinity for all possible remainders after modulo operation
    dist: List[int] = [float("inf")] * MOD
    # Distance from start to itself is 0
    dist[start] = 0

    # Perform BFS traversal
    while q:
        node, steps = q.popleft()

        # Explore all possible multiplication results using the elements in the array
        for num in arr:
            number: int = (num * node) % MOD

            # If the new steps are smaller than the previously recorded distance, update the distance and add to the queue
            if steps + 1 < dist[number]:
                dist[number] = steps + 1
                # If the target number is reached, return the steps
                if number == end:
                    return steps + 1
                q.append((number, steps + 1))

    # If the target number is not reachable, return -1
    return -1


# Example usage
if __name__ == "__main__":
    arr: List[int] = [2, 5, 7]
    start: int = 3
    end: int = 75

    min_step: int = find_min_step(arr=arr, start=start, end=end)
    print(min_step)
