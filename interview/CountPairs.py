# Check if pair with given Sum exists in Array
def Sum(arr, target):
    n = len(arr) 
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if (arr[i]+arr[j]) == target:
                count += 1
    return count

arr = [1,2,3,4,5]
target = 6
print(Sum(arr, target)) # 2