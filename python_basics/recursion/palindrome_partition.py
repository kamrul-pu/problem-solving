"""Palindrome partition."""


def is_palindrome(s: str, first: int, last: int) -> bool:
    while first <= last:
        if s[first] != s[last]:
            return False
        first += 1
        last -= 1
    return True


def func(ind: int, s: str, path: list[str], res: list[list[str]]) -> None:
    if ind == len(s):
        res.append(path.copy())
        return
    for i in range(ind, len(s)):
        if is_palindrome(s=s, first=ind, last=i):
            path.append(s[ind : i + 1])
            func(ind=i + 1, s=s, path=path, res=res)
            path.pop()


if __name__ == "__main__":
    s: str = "aabb"
    res: list[list[str]] = []
    func(ind=0, s=s, path=[], res=res)
    print(res)
