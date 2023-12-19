"""Print Subsequences using recursion."""
res: list[list[int]] = []


def subsequence(arr: list[int], i: int, n: int, ans: list[int]) -> None:
    if i >= n:
        print(ans)
        res.append(ans.copy())
        return
    ans.append(arr[i])
    subsequence(arr, i + 1, n, ans)
    ans.pop()
    subsequence(arr, i + 1, n, ans)


arr: list[int] = [3, 1, 2]
n: int = 3
ans: list[int] = []
subsequence(arr, 0, n, ans)
print("outer answer", res)
