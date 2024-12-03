# Problem Description
# You are given two arrays:

# Array A (values): Represents numbers for which we want to find a least prime number.
# Array B (divisors): Represents numbers that should divide the sum of the numbers in Array A and the least prime.
# Task: For each element in Array A, find the least prime number that can be added to it such that the result is divisible by the corresponding element in Array B.

# Example
# Input:
# plaintext
# Copy code
# Array A: [10, 15, 7]
# Array B: [3, 5, 2]

# Output:
# plaintext
# Copy code
# [2, 2, 3]

# Explanation:
# For the first element:
# A[0] = 10, B[0] = 3
# Least prime addition: 2
# 10 + 2 = 12, which is divisible by 3.
# For the second element:
# A[1] = 15, B[1] = 5
# Least prime addition: 2
# 15 + 2 = 17, which is divisible by 5.
# For the third element:
# A[2] = 7, B[2] = 2
# Least prime addition: 3
# 7 + 3 = 10, which is divisible by 2.

# Algorithm
# Start with a helper function to check if a number is prime.
# Iterate through both arrays simultaneously.
# For each element in A, find the smallest prime number P such that (A[i] + P) % B[i] == 0.
# Store the result for each pair.





# Method 1

# def is_prime(n):    #Helper function

#     if n < 2:
#         return False
    
#     for i in range(0, int(n**0.5)+1):
#         if n%1 == 0:
#             return False
#     return True

# def least_prime_addition(arrA, arrB):
#     res = []

#     for a, b in zip(arrA, arrB):
#         add_prime_number = 2  #take the smallest prime number

#         while (a + add_prime_number) % b != 0:
#             add_prime_number += 1

#             while not is_prime(add_prime_number):
#                 add_prime_number += 1
        
#         res.append(add_prime_number)

#     return res

# # Example Usage
# array_a = [10, 15, 7]
# array_b = [3, 5, 2]
# output = least_prime_addition(array_a, array_b)
# print(output)  # Output: [2, 2, 3]





def sieve_of_eratosthenes(limit):
    """Generate a list of prime numbers up to a given limit using the sieve of Eratosthenes."""
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [x for x in range(limit + 1) if is_prime[x]]

def least_prime_addition_optimized(array_a, array_b, prime_limit=100):
    """Optimized function to find the least prime addition."""
    primes = sieve_of_eratosthenes(prime_limit)  # Precompute primes up to the given limit
    results = []
    
    for a, b in zip(array_a, array_b):
        for prime in primes:
            if (a + prime) % b == 0:
                results.append(prime)
                break
    
    return results

# Example Usage
array_a = [10, 15, 7]
array_b = [3, 5, 2]
output = least_prime_addition_optimized(array_a, array_b, prime_limit=100)
print(output)  # Output: [2, 2, 3]



# Complexity Analysis
# Sieve of Eratosthenes:

# Precomputing primes up to a limit O(Llog(log(L))).

# Checking Divisibility:

# For each pair in array_a and array_b, iterating through the precomputed primes takes O(P), where 𝑃 is the number of primes up to the limit.
# Overall Complexity: O(Llog(log(L))+N⋅P), where L is the sieve limit, N is the array size, and P is the number of primes.
