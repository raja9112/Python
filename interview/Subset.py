# Find whether an array is subset of another array
def SubSetOfArray(arr1, arr2):
    # Method 1
    # s1 = set(arr1)
    # s2 = set(arr2)
    
    # return s2.issubset(s1)
    
    
    # Method 2
    for element in arr2:
        if element not in arr1:
            return False
        return True

array1 = [1, 2, 3, 4, 5, 6]
array2 = [3, 4, 5]

if SubSetOfArray(array1, array2):
    print("Array2 is subset of array1")   # Output
else: print("Array2 is not subset of array1")
