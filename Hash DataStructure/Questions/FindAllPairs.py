# Find all pairs (a, b) in an array such that a % b = k
def Pairs(arr, target):
    n = len(arr) 
 
    for i in range(n):
        for j in range(0, n):
            if i != j and (arr[i]%arr[j]) == target:
                print(f"({arr[i]},{arr[j]})", sep="", end= " ")

arr = [2, 3, 5, 4, 7]
target = 3
print(Pairs(arr, target)) # (3,5) (3,4) (3,7) (7,4)