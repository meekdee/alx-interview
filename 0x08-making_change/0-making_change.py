#!/usr/bin/python3
def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize dp array with a large value (inf) for all indexes except dp[0]
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # 0 coins are needed to make a total of 0

    # Fill dp array
    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still inf, return -1 (total cannot be met)
    return dp[total] if dp[total] != float('inf') else -1
