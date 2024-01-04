# Find the Most Frequent number present in array.

# Approach one - Hash method

# from collections import defaultdict
# def frequency(array):
#     hash_table = defaultdict(int)
    
#     for i in array:
#         hash_table[i] += 1
#         print(hash_table.items())
        
#     max_count = max(hash_table.values())
    
#     result = [(i,"->", j) for i, j in hash_table.items() if j == max_count]
#     return result

# array = [1,2,3,4,1,5,1,6,1,7]
# print(frequency(array))

# Output
# dict_items([(1, 1)])
# dict_items([(1, 1), (2, 1)])
# dict_items([(1, 1), (2, 1), (3, 1)])
# dict_items([(1, 1), (2, 1), (3, 1), (4, 1)])
# dict_items([(1, 2), (2, 1), (3, 1), (4, 1)])
# dict_items([(1, 2), (2, 1), (3, 1), (4, 1), (5, 1)])
# dict_items([(1, 3), (2, 1), (3, 1), (4, 1), (5, 1)])
# dict_items([(1, 3), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1)])
# dict_items([(1, 4), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1)])
# dict_items([(1, 4), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)])
# [(1, '->', 4)]


# Approach two - Native

def frequency(array):
    d = {}
    for i in array:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for num, val in d.items():
        if val > 1:
            print(f"{num} occurs {val} times.")
        
array = [1,2,3,4,1,2,1,6,1,7]
print(frequency(array))

# Output
# 1 occurs 4 times.
# 2 occurs 2 times.