# Move Zeroes to the End of an Array

def move_zeros(arr):
    l = 0
    
    for r in range(len(arr)):
        if arr[r] != 0:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1

    return arr
    

print(move_zeros([0,1,0,3,12]))