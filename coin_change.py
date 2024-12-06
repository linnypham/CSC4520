def coinChange(coins,amount):
    dp = [0]*(amount+1)
            
    for i in range(1,amount+1):
        f = float('inf')
        for coin in coins:
            if coin <= i:
                f = min(f,dp[i-coin])
        if f != float('inf'):
            dp[i] = f+1
        else:
            dp[i] = float('inf')
    if dp[amount] == float('inf'):
        return -1
    else:
        return dp[amount]
    
coins = [1,2,5]
amount = 11
print(coinChange(coins,amount))