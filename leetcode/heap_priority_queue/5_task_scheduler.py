"""
You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n.
Each cycle or interval allows the completion of one task. Tasks can be completed in any order,
but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.

​Return the minimum number of intervals required to complete all tasks.
"""

import heapq
from collections import Counter, deque
from typing import Counter, Deque, List, Tuple


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Initialize a counter to keep track of task frequencies
        count: Counter = Counter(tasks)

        # Create a max-heap (min-heap with negative values) to store task frequencies
        max_heap: List[int] = [
            -cnt for cnt in count.values()
        ]  # Use negative values for max-heap
        heapq.heapify(max_heap)  # Heapify to maintain the max-heap property

        time: int = 0  # Initialize time to track intervals
        q: Deque[Tuple[int, int]] = (
            deque()
        )  # Deque to track delayed tasks (count, available time)

        while max_heap or q:
            time += 1  # Increment time for each interval

            if max_heap:
                cnt = 1 + heapq.heappop(
                    max_heap
                )  # Retrieve and increment task frequency
                if cnt != 0:
                    q.append(
                        (cnt, time + n)
                    )  # Add the task back to the queue with cooling time

            if q and q[0][1] == time:
                # If the first task in the queue is available to be processed
                heapq.heappush(
                    max_heap, q.popleft()[0]
                )  # Push the task back to the max_heap

        return time  # Return the total time intervals required to complete all tasks


# Example usage:
if __name__ == "__main__":
    tasks: List[str] = ["A", "A", "A", "B", "B", "B"]  # Example list of tasks
    n: int = 2  # Cooling time between identical tasks

    solution: Solution = Solution()  # Create an instance of the Solution class
    result: int = solution.leastInterval(
        tasks=tasks, n=n
    )  # Find the minimum intervals required
    print(result)  # Print the result (minimum intervals)
