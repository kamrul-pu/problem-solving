"""Maximum Subarray product."""

from typing import List


class Solution:
    # Brute-force approach to find maximum product of subarray
    def __max_product(self, nums: List[int], n: int) -> int:
        mx_product: int = -1e9
        # Iterate through each element as the starting point of a subarray
        for i in range(n):
            product: int = 1
            # Iterate through elements from the starting point to find subarrays
            for j in range(i, n):
                product *= nums[j]
                # Update the maximum product if the current product is greater
                mx_product = max(mx_product, product)

            # Update the maximum product considering the single-element subarray
            mx_product = max(mx_product, product)

        return mx_product

    # Optimal approach to find maximum product of subarray
    def __max_product_optimal(self, nums: List[int], n: int) -> int:
        mx_product: int = -1e9
        prefix: int = 1
        suffix: int = 1
        # Iterate through the array to find maximum product of subarray
        for i in range(n):
            prefix *= nums[i]
            suffix *= nums[n - i - 1]
            # Update the maximum product if prefix or suffix is greater than the current maximum
            mx_product = max(mx_product, prefix, suffix)

            # Reset prefix or suffix to 1 if it becomes 0
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1

        return mx_product

    # Main function to find maximum product of subarray
    def maxProduct(self, nums: List[int]) -> int:
        n: int = len(nums)
        # Uncomment the appropriate function call based on the approach to use
        # return self.__max_product(nums=nums, n=n)  # Brute-force approach
        return self.__max_product_optimal(nums=nums, n=n)  # Optimal approach


# Main function to test the maxProduct function
if __name__ == "__main__":
    nums: List[int] = [2, 3, -2, 4]
    # nums = [-3, 0, 1, -2]
    # nums = [-2, 0, -1]
    solution: Solution = Solution()
    print(solution.maxProduct(nums=nums))
