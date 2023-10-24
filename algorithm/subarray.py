"""Generate sub array from the array."""

subsets = []


def generate(subset: list[int], i: int, nums: list[int]):
    if i == len(nums):
        subsets.append(subset.copy())
        return
    # ith element is not in subset
    generate(subset, i + 1, nums)
    # ith element in subset
    subset.append(nums[i])
    print("SSSSSSSSSS", subset)
    generate(subset, i + 1, nums)
    # pop the top element cause previous function should have the same value. called backtracking
    subset.pop()


if __name__ == "__main__":
    arr = [1, 2, 3]
    subset = []
    generate(subset, 0, arr)
    print(subsets)
