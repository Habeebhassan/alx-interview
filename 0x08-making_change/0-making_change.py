#!/usr/bin/python3
"""
make change module"""


from collections import deque

def makeChange(coins, total):
    # If total is 0 or less, return 0 (no coins are needed)
    if total <= 0:
        return 0
    
    # Use a queue to perform BFS, start with the total 0 and 0 coins used
    queue = deque([(0, 0)])  # (current_total, number_of_coins)
    visited = set()  # Keep track of visited totals to avoid repetition
    
    # Perform BFS
    while queue:
        current_total, num_coins = queue.popleft()
        
        # Try adding each coin to the current total
        for coin in coins:
            new_total = current_total + coin
            
            # If we exactly reach the total, return the number of coins
            if new_total == total:
                return num_coins + 1
            
            # If new_total is less than the target and hasn't been visited
            if new_total < total and new_total not in visited:
                visited.add(new_total)
                queue.append((new_total, num_coins + 1))
    
    # If we exhaust the BFS without finding the total, return -1
    return -1

