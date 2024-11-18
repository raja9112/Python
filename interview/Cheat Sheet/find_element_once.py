# find_element_once

def find_element_once(arr):

    res = 0
    for i in arr:
        res ^= i
    
    return res


print(find_element_once([4, 3, 4, 3, 2]))  # Output: 2
print(find_element_once([5, 7, 5]))        # Output: 7
print(find_element_once([1, 1, 2, 2, 3]))  # Output: 3
print(find_element_once([8, 8, 10, 10, 12]))  # Output: 12