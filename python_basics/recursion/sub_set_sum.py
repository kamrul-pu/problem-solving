"""Subset sum using recursion."""


def subset_sum(nums: list[int], n: int, i: int, s: int, ans: list[int]) -> None:
    if i == n:
        ans.append(s)
        return
    # not taking the element
    subset_sum(nums=nums, n=n, i=i + 1, s=s, ans=ans)
    # taking the element
    s += nums[i]
    subset_sum(nums=nums, n=n, i=i + 1, s=s, ans=ans)
    # pop back the element
    s -= nums[i]


if __name__ == "__main__":
    nums: list[int] = [3, 1, 2]
    n: int = len(nums)
    ans: list[int] = []
    subset_sum(nums=nums, n=n, i=0, s=0, ans=ans)
    ans.sort()
    print(ans)
