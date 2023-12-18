"""Check if the string is palindrome or not."""

txt: str = "MADAMM"
txt: str = "ABAABD"


def is_palindrome(txt: str) -> bool:
    low: int = 0
    high: int = len(txt) - 1
    while low < high:
        if txt[low] != txt[high]:
            return False
        low += 1
        high -= 1
    return True


print(is_palindrome(txt=txt))


def is_palindrome_recursion(txt: str, i: int, n: int) -> bool:
    if i >= n // 2:
        return True
    if txt[i] != txt[n - i - 1]:
        return False
    return is_palindrome_recursion(txt=txt, i=i + 1, n=n)


print(is_palindrome_recursion(txt=txt, i=0, n=len(txt)))
