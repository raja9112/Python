def swapping(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr)-i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(arr)
                count += 1
    return count


  
print(swapping([8, 5, 2, 7, 4, 1, 6, 10, 3, 9]))
print(swapping([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
print(swapping([3, 1, 2]))
