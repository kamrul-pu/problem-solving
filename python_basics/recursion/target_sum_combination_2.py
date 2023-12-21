"""Target sum combinations."""
ans: dict = {}
nums: list[int] = [10, 1, 2, 7, 6, 1, 5]
nums: list[int] = [1, 1, 1, 2, 2]
n: int = len(nums)


def find_combinations(ind: int, target: int, ds: list[int]) -> None:
    if ind == n:
        if target == 0:
            data = ds.copy()
            key = tuple(data)
            ans[key] = data
            # ans.append(sorted(ds.copy()))
        return
    if nums[ind] <= target:
        ds.append(nums[ind])
        find_combinations(ind=ind + 1, target=target - nums[ind], ds=ds)
        ds.pop()
    find_combinations(ind=ind + 1, target=target, ds=ds)


result: list[list[int]] = []


def find_combinations_2(ind: int, target: int, ds: list[int]) -> None:
    if target == 0:
        result.append(ds.copy())
        return

    for i in range(ind, n):
        if i > ind and nums[i] == nums[i - 1]:
            continue
        if nums[i] > target:
            break
        ds.append(nums[i])
        find_combinations_2(ind=i + 1, target=target - nums[i], ds=ds)
        ds.pop()


if __name__ == "__main__":
    # first sort the data
    nums.sort()
    find_combinations(ind=0, target=8, ds=[])
    print(ans.values())
    find_combinations_2(ind=0, target=4, ds=[])
    print(result)
