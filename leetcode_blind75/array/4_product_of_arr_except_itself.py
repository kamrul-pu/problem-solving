"""Product od array except itself."""

from typing import List


class Solution:
    # Brute-force approach to calculate product of array except itself
    def __f(self, nums: List[int], n: int) -> List[int]:
        result: List[int] = [1] * n
        # Iterate through each element in the array
        for i in range(n):
            product: int = 1
            # Calculate the product of all elements except the current one
            for j in range(n):
                if i == j:
                    continue
                product *= nums[j]

            # Assign the product to the result list
            result[i] = product

        return result

    # Optimal approach to calculate product of array except itself
    def __product_arr(self, nums: List[int], n: int) -> List[int]:
        result: List[int] = [1] * n
        prefix: int = 1

        # Calculate the prefix product
        for i in range(n):
            result[i] *= prefix
            prefix *= nums[i]

        postfix: int = 1

        # Calculate the postfix product and update the result list
        for i in range(n - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result

    # Main function to calculate product of array except itself
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n: int = len(nums)
        # Uncomment the appropriate function call based on the approach to use
        # return self.__f(nums=nums, n=n)  # Brute-force approach
        return self.__product_arr(nums=nums, n=n)  # Optimal approach


# Main function to test the productExceptSelf function
if __name__ == "__main__":
    nums: List[int] = [1, 2, 3, 4]
    solution: Solution = Solution()
    print(solution.productExceptSelf(nums=nums))
