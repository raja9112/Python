# sort_by_min_prime_factor


def sieve_smallest_prime_factor(limit):
    """
    Generate the smallest prime factor (SPF) for every number up to 'limit' using the sieve.
    """
    spf = list(range(limit + 1))  # Initialize SPF array
    for i in range(2, int(limit**0.5) + 1):
        if spf[i] == i:  # 'i' is a prime
            for j in range(i * i, limit + 1, i):
                if spf[j] == j:  # Only update if 'j' hasn't been marked yet
                    spf[j] = i
    return spf

def sort_by_min_prime_factor(arr):
    """
    Sort the array by the smallest prime factor of each element.
    """
    if not arr:  # Handle empty array
        return []

    max_val = max(arr)  # Find the maximum value in the array
    spf = sieve_smallest_prime_factor(max_val)  # Compute SPF up to max_val

    # Sort array using SPF as the key
    sorted_arr = sorted(arr, key=lambda x: spf[x])
    return sorted_arr

# Example Usage
arr = [10, 15, 21, 8, 25, 6]
sorted_arr = sort_by_min_prime_factor(arr)
print(sorted_arr)  # Expected Output: [8, 6, 10, 15, 21, 25]
