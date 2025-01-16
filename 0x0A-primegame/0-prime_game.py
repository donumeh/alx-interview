#!/usr/bin/python3
""" Module for solving prime game question """


def isWinner(x, nums):
    """is Winner function"""
    if x < 1 or not nums:
        return None

    max_num = max(nums)

    # Step 1: Compute primes up to max_num using Sieve of Eratosthenes
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime
    for i in range(2, int(max_num**0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_num + 1, i):
                primes[j] = False

    # Step 2: Precompute the number of primes up to each number
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    # Step 3: Determine the winner for each round
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Step 4: Return the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
