def lexicographic_sort(arr):

    # Time: O(n^2)
    # Space: O(1)

    # for i in range(len(arr)):
    #     for j in range(i+1, len(arr)):
    #         if arr[i] > arr[j]:
    #             arr[i], arr[j] = arr[j], arr[i]

    # return arr


    # Time: O(n log n)
    # Merge Sort Implementation for Lexicographic Sorting
    if len(arr) >1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        lexicographic_sort(left)
        lexicographic_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            
            else:
                arr[k] = right[j]
                j += 1
            
            k += 1

        if i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        if j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr

# Example Usage
words = ["apple", "banana", "cherry", "aquaman"]
print(lexicographic_sort(words))  # Output: ['apple', 'aquaman' 'banana', 'cherry']


