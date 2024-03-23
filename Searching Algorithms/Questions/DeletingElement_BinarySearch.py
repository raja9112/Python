def BinarySearch(arr, element):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        
        mid = (low+high) // 2
        
        if arr[mid] == element:
            # Element found, delete it
            i = mid
            while i < len(arr)-1:
               arr[i] = arr[i+1]        # Shift elements to the left
               i += 1
            arr.pop()           # Remove the last element
            return True         # Return True to indicate successful deletion
        elif arr[mid] < element:
            low = mid + 1
        else: high = mid - 1
        
    return False


arr = [2, 4, 6, 7, 8, 10, 12]
element = 6
print(BinarySearch(arr, element))
# print(arr)  # [2, 4, 7, 8, 10, 12, 12]  without pop