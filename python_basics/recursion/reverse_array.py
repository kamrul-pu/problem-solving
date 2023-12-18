"""Reverse an array"""

nums: list[int] = [1, 2, 3, 4, 2]


def reverse_iter(nums: list[int], n: int) -> None:
    low: int = 0
    high: int = n - 1
    while low < high:
        nums[low], nums[high] = nums[high], nums[low]
        low += 1
        high -= 1


reverse_iter(nums=nums, n=len(nums))
print(nums)


def reverse_recursion(nums: list[int], left: int, right: int) -> None:
    if left >= right:
        return
    nums[left], nums[right] = nums[right], nums[left]
    reverse_recursion(nums=nums, left=left + 1, right=right - 1)


reverse_recursion(nums=nums, left=0, right=len(nums) - 1)
print(nums)
