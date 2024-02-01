# Exponential Search:
# Exponential search is a searching algorithm that works on sorted arrays. 
# It involves two steps: first, finding the range where the target element may be present by doubling the index, 
# and second, performing a binary search within that range.

def ExponentialSearch(arr, target):
     n = len(arr)
     
     if arr[0]==target:
         return 0
     
     i = 0
     while i<n and arr[i] <= target:
         i += 2
         
     return binarySearch(arr, target, i//2, min(i, n-1))

def binarySearch(arr, target, low, high):
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid]<target:
            low = mid +1
        else:
            high = mid -1
            
    return -1

arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target = 14
print(ExponentialSearch(arr, target))