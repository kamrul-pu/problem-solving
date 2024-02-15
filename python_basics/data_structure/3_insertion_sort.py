"""
Implement Insertion Sort and return intermediate states.
Insertion Sort is a simple sorting algorithm that builds the
sorted list one element at a time, from left to right.
It works by repeatedly taking an element from the unsorted
portion and inserting it into its correct position in the sorted portion of the list.
"""

from typing import List


# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value


class Solution:
    # Implementation of Insertion Sort
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        n = len(pairs)
        res = []  # To store the intermediate states of the array

        for i in range(n):
            j = i - 1

            # Move elements that are greater than key one position ahead
            while j >= 0 and pairs[j].key > pairs[j + 1].key:
                pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
                j -= 1

            # Clone and save the entire state of the array at this point
            res.append(pairs[:])

        return res


if __name__ == "__main__":
    p1: Pair = Pair(key=5, value="apple")
    p2: Pair = Pair(key=2, value="banana")
    p3: Pair = Pair(key=9, value="cherry")
    pairs: List[Pair] = [p1, p2, p3]
    print("pairs before sort")
    for pair in pairs:
        print(pair.key, pair.value)
    solution: Solution = Solution()
    pairs: List[Pair] = solution.insertionSort(pairs=pairs)
    print("pairs after sort")
    print("pairs", pairs)
