"""Cherry Pickup. 3D DP."""
INT_MIN: int = float("-inf")

cnt: int = 0


def cherry_pickup(
    i: int,
    j1: int,
    j2: int,
    a: list[list[int]],
    n: int,
    m: int,
    dp: list[list[list[int]]],
) -> int:
    global cnt
    cnt += 1
    if j1 < 0 or j1 >= m or j2 < 0 or j2 >= m:
        return INT_MIN
    if i == n - 1:
        if j1 == j2:
            return a[i][j1]
        else:
            return a[i][j1] + a[i][j2]

    if dp[i][j1][j2] != -1:
        return dp[i][j1][j2]

    maxi: int = INT_MIN
    for dj1 in range(-1, 2, 1):
        for dj2 in range(-1, 2, 1):
            if j1 == j2:
                value: int = a[i][j1]
            else:
                value: int = a[i][j1] + a[i][j2]
            value += cherry_pickup(
                i=i + 1, j1=j1 + dj1, j2=j2 + dj2, a=a, n=n, m=m, dp=dp
            )
            maxi = max(maxi, value)
    dp[i][j1][j2] = maxi
    return dp[i][j1][j2]


if __name__ == "__main__":
    a: list[list[int]] = [
        [2, 3, 1, 2],
        [3, 4, 2, 2],
        [5, 6, 3, 5],
        [5, 6, 2, 9],
    ]
    n: int = len(a)
    m: int = len(a[0])
    dp: list[list[list[int]]] = [
        [[-1 for c1 in range(m)] for c1 in range(m)] for r in range(n)
    ]
    print(dp)
    mx: int = cherry_pickup(i=0, j1=0, j2=m - 1, a=a, n=n, m=m, dp=dp)
    print(mx)
    print(cnt)
    print(dp)
