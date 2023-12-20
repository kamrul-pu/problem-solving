"""Target sum combinations."""
ans: list[list[int]] = []
nums: list[int] = [2, 3, 6, 7]
n: int = len(nums)


def find_combinations(ind: int, target: int, ds: list[int]) -> None:
    if ind == n:
        if target == 0:
            ans.append(ds.copy())
        return
    if nums[ind] <= target:
        ds.append(nums[ind])
        find_combinations(ind=ind, target=target - nums[ind], ds=ds)
        ds.pop()
    find_combinations(ind=ind + 1, target=target, ds=ds)


if __name__ == "__main__":
    find_combinations(ind=0, target=7, ds=[])
    print(ans)
