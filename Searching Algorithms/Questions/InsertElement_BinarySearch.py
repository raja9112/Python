def BinarySearch(arr, element):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        
        mid = (low+high) // 2
        
        if arr[mid] == element:
            return mid
        if arr[mid] > element:
            high = mid - 1
        else: low = mid + 1
        
    # print (low) # 3
    
    
    # The target is not found, so it should be inserted at the position of low
    arr.append(None)    # Add a placeholder to extend the array
    n = len(arr) - 1
    while n > low:
        arr[n] = arr[n-1]   # Shift elements to the right
        n -= 1
    arr[low] = element  # Insert the element at the correct position
    return low          # Return the index where the element is inserted


    # Method 2
    #  arr.insert(low, target)        # array.insert(index, element)

arr = [2, 4, 6, 8, 10, 12]
element = 8
print(BinarySearch(arr, element))
# print(arr)   # [2, 4, 6, 8, 8, 10, 12]   Before inserting the element