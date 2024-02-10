"""Array 3 sum problem."""

from typing import List


class Solution:
    def __f(self, nums: List[int], n: int) -> List[List[int]] | List:
        ans: List[List[int]] = []
        nums.sort()  # Sort the input list in ascending order
        for i in range(n):
            if (
                i > 0 and nums[i] == nums[i - 1]
            ):  # Skip duplicate elements to avoid duplicate triplets
                continue
            j: int = i + 1  # Set the left pointer to the element after nums[i]
            k: int = n - 1  # Set the right pointer to the last element
            while (
                j < k
            ):  # Iterate until the left pointer is less than the right pointer
                three_sum: int = (
                    nums[i] + nums[j] + nums[k]
                )  # Calculate the sum of three elements
                if (
                    three_sum < 0
                ):  # If the sum is less than 0, move the left pointer to the right to increase the sum
                    j += 1
                elif (
                    three_sum > 0
                ):  # If the sum is greater than 0, move the right pointer to the left to decrease the sum
                    k -= 1
                else:  # If the sum is equal to 0, found a triplet
                    ans.append(
                        [nums[i], nums[j], nums[k]]
                    )  # Add the triplet to the answer list
                    j += 1  # Move the left pointer to the right
                    k -= 1  # Move the right pointer to the left
                    # Skip duplicate elements to avoid duplicate triplets
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return ans

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n: int = len(nums)
        return self.__f(nums=nums, n=n)


# Main function to test the threeSum function
if __name__ == "__main__":
    nums: List[int] = [-1, 0, 1, 2, -1, -4]
    solution: Solution = Solution()
    print(solution.threeSum(nums=nums))
