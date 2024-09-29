# Ninja Technique for 2D Dynamic Programming
from typing import List


def max_merit(task: List[List[int]], day: int, last: int, memo: List[List[int]]) -> int:
    """
    Calculate the maximum merit using recursion with memoization.

    :param task: A 2D list where task[day][task_number] represents the merit for a task on a specific day.
    :param day: The current day (0-indexed).
    :param last: The last task that was performed (0: task 1, 1: task 2, 2: task 3, 3: none).
    :param memo: A 2D list for memoization to store already computed results.
    :return: The maximum merit achievable up to the given day.
    """
    # Base case: If it's the first day, return the maximum value of the first row
    if day == 0:
        return max(task[0][i] for i in range(3) if i != last)

    # If the result for the current state is already memoized, return it
    if memo[day][last] != -1:
        return memo[day][last]

    # Initialize maximum merit for the current day
    maxi = 0

    # Iterate through the possible tasks on the current day
    for i in range(3):
        if i != last:
            # Calculate the merit for the current task
            point = task[day][i] + max_merit(task, day - 1, i, memo)
            maxi = max(maxi, point)

    # Memoize the result for the current state
    memo[day][last] = maxi
    return maxi


def max_merit_tabulation(task: List[List[int]], n: int) -> int:
    """
    Calculate the maximum merit using dynamic programming (tabulation).

    :param task: A 2D list where task[day][task_number] represents the merit for a task on a specific day.
    :param n: The number of days/tasks available.
    :return: The maximum merit achievable by the last day.
    """
    dp: List[List[int]] = [[0 for _ in range(4)] for _ in range(n)]

    # Initialize the first day
    dp[0][0] = max(task[0][1], task[0][2])
    dp[0][1] = max(task[0][0], task[0][2])
    dp[0][2] = max(task[0][0], task[0][1])
    dp[0][3] = max(task[0][0], task[0][1], task[0][2])

    # Fill the DP table
    for day in range(1, n):
        for last in range(4):
            for t in range(3):
                if t != last:
                    dp[day][last] = max(dp[day][last], task[day][t] + dp[day - 1][t])

    return dp[n - 1][3]


def max_merit_optimal(task: List[List[int]], n: int) -> int:
    """
    Calculate the maximum merit using optimized space complexity.

    :param task: A 2D list where task[day][task_number] represents the merit for a task on a specific day.
    :param n: The number of days/tasks available.
    :return: The maximum merit achievable by the last day.
    """
    prev: List[int] = [0] * 4

    # Initialize the first day
    prev[0] = max(task[0][1], task[0][2])
    prev[1] = max(task[0][0], task[0][2])
    prev[2] = max(task[0][0], task[0][1])
    prev[3] = max(task[0][0], task[0][1], task[0][2])

    # Calculate for each subsequent day
    for day in range(1, n):
        temp: List[int] = [0] * 4
        for last in range(4):
            for t in range(3):
                if t != last:
                    temp[last] = max(temp[last], task[day][t] + prev[t])
        prev = temp

    return prev[3]


if __name__ == "__main__":
    # Example input values
    n: int = 2
    task: List[List[int]] = [
        [10, 50, 1],
        [5, 100, 11],
    ]

    # Initialize memoization
    memo: List[List[int]] = [
        [-1 for _ in range(len(task[0]) + 1)] for _ in range(len(task))
    ]

    # Calculate and print the maximum merit using different methods
    print(
        "Max Merit (Recursion + Memoization):",
        max_merit(task=task, day=len(task) - 1, last=3, memo=memo),
    )
    print("Max Merit (Tabulation):", max_merit_tabulation(task=task, n=len(task)))
    print("Max Merit (Optimal):", max_merit_optimal(task=task, n=n))
