"""Minimum coins to react traget amount."""

def min_coins(i:int, amount:int, coins:list[int], memo={})->int:
    if i==0:
        if amount%coins[i]==0:
            return amount//coins[i]
        return float("inf")

    key:tuple[int] = (i, amount)
    if key in memo:
        return memo[key]

    not_take:int = 0 + min_coins(i=i-1, amount=amount, coins=coins, memo=memo)
    take:int = float("inf")
    if coins[i]<=amount:
        take = 1 + min_coins(i=i, amount=amount-coins[i], coins=coins, memo=memo)

    memo[key] = min(take, not_take)    
    return memo[key]

def min_coins_tabulation(coins:list[int], n:int, amount:int)->int:
    dp:list[list[int]] = [[0 for col in range(amount+1)] for row in range(n)]

    for t in range(amount+1):
        if t%coins[0] == 0:
            dp[0][t] = t//coins[0]
        else:
            dp[0][t] = float("inf")
    
    for i in range(1,n):
        for t in range(amount+1):
            not_take:int = 0 + dp[i-1][t]
            take:int = float("inf")
            if coins[i]<=t:
                take = 1 + dp[i][t-coins[i]]
            dp[i][t] = min(take, not_take)
    
    return dp[n-1][amount]

def min_coins_optimal(coins:list[int], n:int, amount:int)->int:
    prev:list[int] = [0 for col in range(amount+1)]
    cur:list[int] = [0 for col in range(amount+1)]
    for t in range(amount+1):
        if t%coins[0] == 0:
            prev[t] = t//coins[0]
        else:
            prev[t] = float("inf")
    
    for i in range(1,n):
        for t in range(amount+1):
            not_take:int = 0 + prev[t]
            take:int = float("inf")
            if coins[i]<=t:
                take = 1 + cur[t-coins[i]]
            cur[t] = min(take, not_take)
        prev = cur.copy()

    return prev[amount]

if __name__ == "__main__":
    coins:list[int] = [1,2,3]
    amount:int = 290
    n:int = len(coins)
    mn_coin:int = min_coins(i=n-1, amount=amount, coins=coins, memo={})
    print(mn_coin)
    print(min_coins_tabulation(coins=coins, n=n, amount=amount))
    print(min_coins_optimal(coins=coins, n=n, amount=amount))
