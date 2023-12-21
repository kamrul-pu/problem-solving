def subset_generation(
    nums: list[int], n: int, i: int, subset: list[int], subsets: list[int]
) -> None:
    if i == n:
        data = sorted(subset.copy())
        key = tuple(data)
        subsets[key] = data
        return
    subset_generation(nums=nums, n=n, i=i + 1, subset=subset, subsets=subsets)
    subset.append(nums[i])
    subset_generation(nums=nums, n=n, i=i + 1, subset=subset, subsets=subsets)
    subset.pop()


def subset_generation_optimal(
    nums: list[int], n: int, ind: int, subset: list[int], subsets: list[list[int]]
) -> None:
    subsets.append(subset.copy())
    for i in range(ind, n):
        if i != ind and nums[i] == nums[i - 1]:
            continue
        subset.append(nums[i])
        subset_generation_optimal(
            nums=nums, n=n, ind=i + 1, subset=subset, subsets=subsets
        )
        subset.pop()


if __name__ == "__main__":
    nums: list[int] = [1, 2, 2]
    n: int = len(nums)
    # subsets: list[list[int]] = {}
    # subset_generation(nums=nums, n=n, i=0, subset=[], subsets=subsets)
    # print(sorted(subsets.values()))
    subsets: list[list[int]] = []
    subset_generation_optimal(nums=nums, n=n, ind=0, subset=[], subsets=subsets)
    print(subsets)
