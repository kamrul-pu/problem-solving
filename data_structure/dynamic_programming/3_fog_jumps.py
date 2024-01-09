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


if __name__ == "__main__":
    n: int = 4
    arr: list[int] = [10, 20, 30, 10]

    # Calculate and print the minimum energy required for the entire fog jump sequence
    min_cost: int = min_energy(ind=n - 1, arr=arr)
    print("Minimum energy required:", min_cost)
