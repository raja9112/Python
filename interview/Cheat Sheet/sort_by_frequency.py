# Sort the array elements in descending order according to their frequency of occurrence

from collections import Counter

def sort_by_frequency(arr):

    d = Counter(arr)


    # -x[1] is used to sort by freq in descending and x[0] is used to sort element in ascending order
    sorted_freq = sorted(d.items(),key = lambda x: (-x[1], x[0]))

    res = []
    for element, freq in sorted_freq:
        res.extend([element] * freq)


    return res


arr = [4, 5, 6, 5, 4, 3, 1, 1, 1, 4, 5]
sorted_arr = sort_by_frequency(arr)
print(f"Sorted array: {sorted_arr}")


# Time: O(n + m log m)
# Space: O(m)

