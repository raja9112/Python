def primes_in_range(start, end):
    """
    Find all prime numbers in the range [start, end].
    """
    if end < 2:
        return []  # No primes below 2
    
    # Handle negative start values
    start = max(start, 2)

    # Create a boolean array for primality check
    is_prime = [True] * (end + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes

    for i in range(2, int(end**0.5) + 1):
        if is_prime[i]:
            # Mark all multiples of i as non-prime
            for j in range(i * i, end + 1, i):
                is_prime[j] = False

    # Collect primes in the range
    primes = [x for x in range(start, end + 1) if is_prime[x]]
    return primes

# Test the function
print(primes_in_range(10, 50))  # Output: [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
print(primes_in_range(-10, 20)) # Output: [2, 3, 5, 7, 11, 13, 17, 19]
print(primes_in_range(30, 30))  # Output: []
