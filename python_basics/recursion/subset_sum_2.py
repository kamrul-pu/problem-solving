def subset_generation(
    nums: list[int], n: int, i: int, subset: list[int], subsets: list[int]
) -> None:
    if i == n:
        subsets.append(subset.copy())
        return
    subset_generation(nums=nums, n=n, i=i + 1, subset=subset, subsets=subsets)
    subset.append(nums[i])
    subset_generation(nums=nums, n=n, i=i + 1, subset=subset, subsets=subsets)
    subset.pop()


if __name__ == "__main__":
    nums: list[int] = [1, 2, 2]
    n: int = len(nums)
    subsets: list[list[int]] = []
    subset_generation(nums=nums, n=n, i=0, subset=[], subsets=subsets)
    print(subsets)
