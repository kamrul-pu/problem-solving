"""
You are given a sorted array arr of length n, which contains positive integer positions of n gas stations on the X-axis.
You are also given an integer k. You have to place 'k' new gas stations on the X-axis.
You can place them anywhere on the non-negative side of the X-axis, even on non-integer positions.
Let 'dist' be the maximum value of the distance between adjacent gas stations after adding 'k' new gas stations.

Find the minimum value of dist.
"""

import heapq
from typing import List, Deque, Tuple


def brute(arr: List[int], k: int) -> int:
    n: int = len(arr)  # Length of the sorted array arr
    how_many: List[int] = [0] * (
        n - 1
    )  # Array to track how many new stations are added between each pair of existing stations

    # Iterate to place k new gas stations
    for gas_station in range(1, k + 1):
        max_section: int = -1
        max_ind: int = -1

        # Find the section (between existing gas stations) with the maximum potential length
        for i in range(n - 1):
            diff: float = (
                arr[i + 1] - arr[i]
            )  # Distance between current and next existing gas station
            section_length: float = diff / (
                how_many[i] + 1
            )  # Length per new gas station in this section

            # Update the maximum section length and its index
            if section_length > max_section:
                max_section = section_length
                max_ind = i

        how_many[
            max_ind
        ] += 1  # Place a new gas station in the section with the maximum length found

    max_ans: float = -1

    # Calculate the maximum distance (dist) after placing all k new gas stations
    for i in range(n - 1):
        diff: float = (
            arr[i + 1] - arr[i]
        )  # Distance between current and next existing gas station
        section_length: float = diff / (
            how_many[i] + 1
        )  # Length per new gas station in this section
        max_ans = max(max_ans, section_length)  # Update the maximum distance

    return max_ans  # Return the minimized maximum distance


def better(arr: List[int], k: int) -> float:
    n: int = len(arr)  # Length of the sorted array arr
    how_many: List[int] = [0] * (
        n - 1
    )  # Array to track how many new stations are added between each pair of existing stations

    pq: List[Tuple[float, int]] = []  # Min-heap to store (distance, index) tuples

    # Initialize the heap with distances between consecutive gas stations
    for i in range(n - 1):
        dist = arr[i + 1] - arr[i]
        heapq.heappush(pq, (-1 * dist, i))

    # Place k new gas stations
    for i in range(1, k + 1):
        dist, ind = heapq.heappop(
            pq
        )  # Get the smallest distance and its index from the heap
        how_many[ind] += 1  # Increment the count of new stations in this section
        diff: float = arr[ind + 1] - arr[ind]
        section_length: float = diff / (how_many[ind] + 1)
        heapq.heappush(
            pq, (-1 * section_length, ind)
        )  # Push updated section back into the heap

    return heapq.heappop(pq)[0] * -1


def number_of_gas_station(arr: List[int], dist: int, n: int) -> int:
    cnt: int = 0
    for i in range(1, n):
        number_in_between: int = (arr[i] - arr[i - 1]) // dist
        if ((arr[i] - arr[i - 1]) / dist) == number_in_between * dist:
            number_in_between -= 1
        cnt += number_in_between

    return cnt


def optimal(arr: List[int], k: int) -> float:
    n: int = len(arr)  # Length of the sorted array arr
    low: float = 0
    high: float = arr[0]
    for i in range(n - 1):
        high = max(high, (arr[i + 1] - arr[i]))

    diff: float = 1e-6
    while high - low > diff:
        mid: float = (low + high) / 2.0
        cnt: int = number_of_gas_station(arr, mid, n)
        if cnt > k:
            low = mid
        else:
            high = mid

    return high


def minimiseMaxDistance(arr: List[int], k: int) -> float:
    return optimal(arr, k)


# Example usage:
k: int = 5
arr: List[int] = [1, 13, 17, 23]
print(minimiseMaxDistance(arr, k))  # Output: 1.0
