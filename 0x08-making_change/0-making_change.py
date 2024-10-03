#!/usr/bin/python3
def makeChange(coins, total):
    """
    Determine fewest coins to 
    meet the total.
    Args:
    coins (list): Values of coins
    total (int): Total to meet
    Returns:
    int: Fewest number of coins
    or -1 if total can't be met.
    """
    if total <= 0:
        return 0

    # Initialize dp array with 
    # size total + 1, filled 
    # with inf to represent 
    # unreachable totals
    dp = [float('inf')] * (total + 1)
    
    # To make total 0, we need 0 
    # coins
    dp[0] = 0
    
    # Compute minimum coins 
    # needed for each amount
    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If total can't be met, 
    # return -1, else return dp[total]
    return dp[total] if dp[total] != float('inf') else -1
