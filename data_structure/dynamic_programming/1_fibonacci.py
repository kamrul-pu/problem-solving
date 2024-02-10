# Fibonacci number using dynamic programming tabulation.

# Global variables for counting function calls
cnt: int = 0

# Memoization table for the first approach
fib: list[int] = [-1] * 101


# Approach 1: Recursion with Memoization
def fibo(n: int) -> int:
    global cnt
    cnt += 1
    # Base case: return n for 0 and 1
    if n <= 1:
        return n
    # Check if the value is already calculated
    if fib[n] != -1:
        return fib[n]
    # Calculate and memoize the result
    fib[n] = fibo(n - 1) + fibo(n - 2)
    return fib[n]


# Approach 2: Recursion with Memoization using explicit memo dictionary
def fibo_memo(n: int, memo: dict = {}) -> int:
    global cnt
    cnt += 1
    # Base case: return n for 0 and 1
    if n < 2:
        return n
    # Check if the value is already calculated in the memo dictionary
    if n in memo:
        return memo[n]
    # Calculate and memoize the result
    memo[n] = fibo_memo(n - 1) + fibo_memo(n - 2)
    return memo[n]


# Approach 3: Dynamic Programming Tabulation
def fib2(n: int) -> int:
    # Initialize a list for storing Fibonacci numbers
    dp: list[int] = [0] * (n + 1)
    # Base cases
    dp[0] = 0
    dp[1] = 1
    # Fill the list using tabulation
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    # Return the result for the nth Fibonacci number
    return dp[n]


def fib3(n: int) -> int:
    # Base case: return n for 0 and 1
    if n <= 1:
        return n

    # Initialize variables for the two previous Fibonacci numbers
    a: int = 0
    b: int = 1

    # Iterate from 2 to n to calculate Fibonacci numbers iteratively
    for i in range(2, n + 1):
        # Calculate the current Fibonacci number
        cur_i: int = a + b
        # Update variables for the next iteration
        a = b
        b = cur_i

    # Return the result for the nth Fibonacci number
    return b


if __name__ == "__main__":
    # Test each approach for calculating the 5th Fibonacci number
    print(fibo(5))
    print("Function calls (Approach 1):", cnt)

    print(fibo_memo(5))
    print("Function calls (Approach 2):", cnt)

    print(fib2(20))
    print(fib3(20))
