# Find whether an array is subset of another array using hash table
def isSubset(arr1, arr2):
    hash_table = {}
    
    for element in arr1:
        hash_table[element] = True # It will save true for all key present in arr1
        
    for i in arr2:
        if i not in hash_table:
            return False
    return hash_table.values   # True
    
    

array1 = [1, 2, 3, 4, 5, 6]
array2 = [3, 4, 5]

if isSubset(array1, array2):
    print("Array2 is a subset of array 1")
else:
    print("Array2 is not a subset of Array1")

