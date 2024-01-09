INT_MAX: int = 999999


def min_energy(ind: int, arr: list[int], memo: dict = {}) -> int:
    """
    Calculate the minimum energy required to traverse a sequence of fog jumps.

    Args:
        ind (int): Current index in the array.
        arr (list[int]): Array representing fog jump heights.
        memo (dict): Memoization dictionary to store already calculated results.

    Returns:
        int: Minimum energy required to traverse the fog jumps up to the current index.
    """
    # Base case: Reached the beginning of the array
    if ind == 0:
        return 0

    # Check if the result for the current index is already memoized
    if ind in memo:
        return memo[ind]

    # Calculate the energy required for the current index by considering both left and right jumps
    left: int = min_energy(ind=ind - 1, arr=arr, memo=memo) + abs(
        arr[ind] - arr[ind - 1]
    )
    right: int = (
        min_energy(ind=ind - 2, arr=arr, memo=memo) + abs(arr[ind] - arr[ind - 2])
        if ind > 1
        else INT_MAX
    )

    # Memoize the result and return the minimum energy for the current index
    memo[ind] = min(left, right)
    return memo[ind]


def find_mn_cost(n: int, arr: list[int]) -> int:
    dp: list[int] = [-1] * (n + 1)
    dp[0] = 0
    for i in range(1, n):
        fs: int = dp[i - 1] + abs(arr[i] - arr[i - 1])
        ss: int = dp[i - 2] + abs(arr[i] - arr[i - 2]) if i > 1 else INT_MAX
        dp[i] = min(fs, ss)

    return dp[n - 1]


def find_mn_optimal(n: int, arr: list[int]) -> int:
    prev_2i: int = 0
    prev_i: int = 0
    cur_i: int = 0
    for i in range(1, n):
        fs: int = prev_i + abs(arr[i] - arr[i - 1])
        ss: int = prev_2i + abs(arr[i] - arr[i - 2]) if i > 1 else INT_MAX
        cur_i = min(fs, ss)
        prev_2i = prev_i
        prev_i = cur_i

    return prev_i


if __name__ == "__main__":
    n: int = 4
    arr: list[int] = [10, 20, 30, 10]

    # Calculate and print the minimum energy required for the entire fog jump sequence
    min_cost: int = min_energy(ind=n - 1, arr=arr)
    print("Minimum energy required:", min_cost)
    print("find min cost", find_mn_cost(n=n, arr=arr))
    print("find cost space optimation", find_mn_optimal(n=n, arr=arr))
