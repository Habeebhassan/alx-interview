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

    amount = 1
    while amount <= total:
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
                # Break if we found a solution for this amount
                break
        amount += 1

    # Return result
    if dp[total] == float('inf'):
        return -1
    return dp[total]
