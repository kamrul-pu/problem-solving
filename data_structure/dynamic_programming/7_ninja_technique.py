# Ninja Technique for 2D Dynamic Programming


def max_merit(task: list[list[int]], day: int, last: int, memo: list[list[int]]) -> int:
    # Base case: If it's the first day, return the maximum value of the first row
    if day == 0:
        maxi: int = 0
        for i in range(3):
            if i != last:
                maxi = max(maxi, task[0][i])
        return maxi

    # If the result for the current state is already memoized, return it
    if memo[day][last] != -1:
        return memo[day][last]

    # Initialize maximum merit for the current day
    maxi: int = 0

    # Iterate through the possible tasks on the current day
    for i in range(3):
        if i != last:
            # Calculate the merit for the current task and recursively call the function for the previous day
            point: int = task[day][i] + max_merit(
                task=task, day=day - 1, last=i, memo=memo
            )
            maxi = max(maxi, point)

    # Memoize the result for the current state
    memo[day][last] = maxi

    return maxi


def max_merit_tabulation(task: list[list[int]], n: int) -> int:
    dp: list[list[int]] = [[-1 for _ in range(4)] for row in range(n)]
    dp[0][0] = max(task[0][1], task[0][2])
    dp[0][1] = max(task[0][0], task[0][2])
    dp[0][2] = max(task[0][0], task[0][1])
    dp[0][3] = max(task[0][0], task[0][1], task[0][2])

    for day in range(1, n):
        for last in range(4):
            dp[day][last] = 0
            maxi: int = 0
            for t in range(3):
                if t != last:
                    point: int = task[day][t] + dp[day - 1][t]
                    dp[day][last] = max(dp[day][last], point)

    return dp[n - 1][3]


def max_merit_optimal(task: list[list[int]], n: int) -> int:
    prev: list[int] = [0] * 4
    prev[0] = max(task[0][1], task[0][2])
    prev[1] = max(task[0][0], task[0][2])
    prev[2] = max(task[0][0], task[0][1])
    prev[3] = max(task[0][0], task[0][1], task[0][2])

    for day in range(1, n):
        temp: list[int] = [0] * 4
        for last in range(4):
            temp[last] = 0
            for t in range(3):
                if t != last:
                    temp[last] = max(temp[last], task[day][t] + prev[t])
        prev = temp

    return prev[3]


if __name__ == "__main__":
    # Input values
    n: int = 2
    task: list[list[int]] = [
        [10, 50, 1],
        [5, 100, 11],
    ]

    # Initialize memoization
    memo: list[list[int]] = [
        [-1 for _ in range(len(task[0]) + 1)] for row in range(len(task))
    ]
    print(memo)
    print(max_merit(task=task, day=len(task) - 1, last=3, memo=memo))
    print(max_merit_tabulation(task=task, n=len(task)))
    print(max_merit_optimal(task=task, n=n))
