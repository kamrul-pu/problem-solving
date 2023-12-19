"""Find sum from the given list."""

nums: list[int] = [1, 2, 1]


def given_sum(i: int, n: int, arr: list[int], sum: int, s) -> None:
    if i == n:
        if s == sum:
            print(arr)
        return
    # take the element
    arr.append(nums[i])
    # add current one
    s += nums[i]
    given_sum(i + 1, n, arr, sum, s)
    # remove from list and reduce from some to give the clean list
    arr.pop()
    s -= nums[i]
    # doest not take the element
    given_sum(i + 1, n, arr, sum, s)


given_sum(0, len(nums), [], 2, 0)
