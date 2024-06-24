"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
"""

from typing import List, Set, Tuple


class Solution:
    def __burte(self, nums: List[int], target: int) -> List[List[int]]:
        n: int = len(nums)
        ans: Set[Tuple[int]] = set()

        # Iterate through all possible combinations of four indices (i, j, k, l)
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                for k in range(j + 1, n - 1):
                    for l in range(k + 1, n):
                        # Check if the sum of selected elements equals the target
                        if (nums[i] + nums[j] + nums[k] + nums[l]) == target:
                            # Sort the quadruplet and add it to the set (to ensure uniqueness)
                            temp = [nums[i], nums[j], nums[k], nums[l]]
                            temp.sort()
                            ans.add(tuple(temp))

        # Convert the set of tuples to a list of lists and return
        return list(ans)

    def __better(self, nums: List[int], target: int) -> List[List[int]]:
        n: int = len(nums)
        ans: Set[Tuple[int]] = set()

        # Iterate through all possible combinations of three indices (i, j, k)
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                st: Set[int] = set()
                for k in range(j + 1, n):
                    # Calculate the fourth element required to reach the target sum
                    fourth: int = target - (nums[i] + nums[j] + nums[k])
                    if fourth in st:
                        # If the fourth element exists in the set, add the sorted quadruplet to the result
                        temp = [nums[i], nums[j], nums[k], fourth]
                        temp.sort()
                        ans.add(tuple(temp))
                    st.add(nums[k])  # Add nums[k] to the set for future reference

        # Convert the set of tuples to a list of lists and return
        return list(ans)

    def __optimal(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # Sort the input array
        n: int = len(nums)
        ans: List[List[int]] = []

        # Iterate through all possible combinations of two indices (i, j) and use two pointers for the other two indices
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates for the first element

            for j in range(i + 1, n - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue  # Skip duplicates for the second element

                k: int = j + 1  # Initialize the left pointer
                l: int = n - 1  # Initialize the right pointer

                while k < l:
                    s: int = nums[i] + nums[j] + nums[k] + nums[l]

                    if s == target:
                        # Found a valid quadruplet, add it to the result
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1  # Skip duplicates for the third element
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1  # Skip duplicates for the fourth element
                    elif s < target:
                        k += 1  # Move the left pointer to the right
                    else:
                        l -= 1  # Move the right pointer to the left

        return ans

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        return self.__optimal(
            nums, target
        )  # Call the optimal function to find four sums


if __name__ == "__main__":
    nums: List[int] = [1, 0, -1, 0, -2, 2]
    target: int = 0
    solution: Solution = Solution()
    result: List[List[int]] = solution.fourSum(nums=nums, target=target)
    print(result)
