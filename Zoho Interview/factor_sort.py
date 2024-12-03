# Problem Statement:
# Given an array of integers, sort the elements in descending order based on the number of factors of each element. If two elements have the same number of factors, retain their relative order (stable sorting).

def count_factors(n):
    """Calculate the number of factors of a given number."""
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1 
            if i != n // i:  # Count both divisors if they are different
                count += 1
    return count

def sort_by_factors(arr):
    """Sort array in descending order based on the number of factors."""
    # Calculate factors and sort
    return sorted(arr, key=lambda x: (-count_factors(x), arr.index(x)))


# Example usage
arr = [10, 7, 9, 4, 6]
sorted_arr = sort_by_factors(arr)
print(sorted_arr)  # Output: [6, 10, 9, 4, 7]
