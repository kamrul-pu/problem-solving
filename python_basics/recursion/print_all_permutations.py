"""Print all possible permutations."""
from collections import defaultdict


def permutations(nums: list[int], n: int, ds: int, mp: dict, ans: list[int]) -> None:
    if len(ds) == n:
        print(ds)
        ans.append(ds.copy())
        return
    for i in range(n):
        if not mp[i]:
            mp[i] = True
            ds.append(nums[i])
            permutations(nums=nums, n=n, ds=ds, mp=mp, ans=ans)
            ds.pop()
            mp[i] = False


if __name__ == "__main__":
    nums: list[int] = [1, 2, 3]
    n: int = len(nums)
    ans: list[list[int]] = []
    permutations(nums=nums, n=n, ds=[], mp=defaultdict(bool), ans=ans)
    print(ans)
