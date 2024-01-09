INT_MAX: int = 999999


def find_min(ind: int, k: int, arr: list[int], memo: dict = {}) -> int:
    """
    Calculate the minimum number of steps required for a frog to reach the last index,
    considering it can jump a maximum of 'k' indices in a single jump.

    Args:
        ind (int): Current index in the array.
        k (int): Maximum distance the frog can jump in a single jump.
        arr (list[int]): Array representing the positions.
        memo (dict): Memoization dictionary to store already calculated results.

    Returns:
        int: Minimum number of steps required for the frog to reach the last index.
    """
    # Base case: Reached the beginning of the array
    if ind == 0:
        return 0

    # Check if the result for the current index is already memoized
    if ind in memo:
        return memo[ind]

    mn_steps: int = INT_MAX

    # Iterate through possible jumps within the range of 'k'
    for i in range(1, k + 1):
        # Calculate the steps for the current jump and update the minimum steps
        current_steps: int = (
            find_min(ind=ind - i, k=k, arr=arr, memo=memo)
            + abs(arr[ind] - arr[ind - i])
            if ind - i >= 0
            else INT_MAX
        )
        mn_steps = min(mn_steps, current_steps)

    # Memoize the result and return the minimum steps for the current index
    memo[ind] = mn_steps
    return memo[ind]


if __name__ == "__main__":
    n: int = 5
    k: int = 3
    arr: list[int] = [10, 30, 40, 50, 20]

    # Calculate and print the minimum number of steps required for the frog to reach the last index
    print("Minimum steps:", find_min(ind=n - 1, k=k, arr=arr))
