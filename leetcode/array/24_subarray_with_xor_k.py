"""
Given an array ‘A’ consisting of ‘N’ integers and an integer ‘B’, find the number of subarrays of array ‘A’ whose bitwise XOR( ⊕ ) of all elements is equal to ‘B’.

A subarray of an array is obtained by removing some(zero or more) elements from the front and back of the array.
"""

from collections import defaultdict
from typing import List, Dict


def subarraysWithSumK(a: List[int], b: int) -> int:
    n: int = len(a)
    ans: int = 0
    hsh: Dict[int, int] = defaultdict(int)
    hsh[0] = 1  # Initialize the default value in the hash map to handle XOR-based sums
    xr: int = 0  # Initialize the cumulative XOR value
    for i in range(n):
        xr = xr ^ a[i]  # Update the cumulative XOR with the current element
        x: int = xr ^ b  # Calculate the target XOR value to find in the hash map
        ans += hsh[
            x
        ]  # Add the count of subarrays found so far that match the target XOR
        hsh[xr] += 1  # Update the hash map to include the current cumulative XOR

    return ans


# Example usage:
nums: List[int] = [4, 2, 2, 6, 4]
print(subarraysWithSumK(a=nums, b=6))
