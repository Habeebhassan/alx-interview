#!/usr/bin/python3

def makeChange(coins, total):
    """
    Determine fewest coins to 
    meet the total.
    
    Args:
        coins (list): Values of coins.
        total (int): Total to meet.
    
    Returns:
        int: Fewest number of coins
        or -1 if total can't be met.
    """
    if total <= 0:
        return 0

    # Initialize dp array
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case

    # Compute minimum coins needed
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # Return result
    return dp[total] if dp[total] != float('inf') else -1
