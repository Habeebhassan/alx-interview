#!/usr/bin/python3
"""
Prime Games for algorithm check
"""


def isWinner(x, nums):
    """
    Determine the winner of the prime removal game.

    Args:
        x (int): Number of rounds.
        nums (list): List of numbers, each representing
        n for the rounds.

    Returns:
        str: The name of the player that won the
        most rounds ("Maria" or "Ben").
        None: If both players win the same number of rounds.
    """
    # Step 1: Precompute prime numbers up to the maximum 
    # value of n using the Sieve of Eratosthenes
    max_n = max(nums) if nums else 0
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes

    # Applying the Sieve of Eratosthenes
    for i in range(2, int(max_n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_n + 1, i):
                sieve[j] = False

    # Step 2: Count how many primes up to each number n
    prime_count_up_to = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count_up_to[i] = prime_count_up_to[i - 1] + (1 if sieve[i] else 0)

    # Step 3: Determine the winner for each round
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Get the number of primes up to n
        prime_count = prime_count_up_to[n]

        # If the number of primes is odd, Maria wins 
        # (she goes first); if even, Ben wins
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Step 4: Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
