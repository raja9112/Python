# count_triangles

def count_triangles(arr):
    # Step 1: Sort the array
    arr.sort()
    n = len(arr)
    count = 0

    # Step 2: Iterate from the end, fixing the largest side
    for k in range(n - 1, 1, -1):
        i = 0
        j = k - 1

        # Step 3: Two-pointer approach
        while i < j:
            if arr[i] + arr[j] > arr[k]:
                # All pairs (i, i+1, ..., j) will form a triangle
                count += (j - i)
                j -= 1  # Decrease the right pointer
            else:
                i += 1  # Increase the left pointer

    return count

# Example usage
arr = [4, 6, 3, 7]
print(count_triangles(arr))  # Output: 3
