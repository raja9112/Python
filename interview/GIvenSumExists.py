# Check if pair with given Sum exists in Array
def Sum(arr, target):
    n = len(arr) 
    
    for i in range(n):
        for j in range(i+1, n):
            if (arr[i]+arr[j]) == target:
                print(f"The target {target} meets when adding {arr[i]} and {arr[j]}.")
                
    return 0

usr = int(input("How many elements do you want add? "))
arr=[]
for i in range(usr):
    arr.append(int(input(f"Enter element {i}: ")))
    
target = int(input("Enter the target number: "))
    
Sum(arr, target)
# Output
# How many elements do you want add? 5
# Enter element 0: 1
# Enter element 1: 2
# Enter element 2: 3
# Enter element 3: 4
# Enter element 4: 5
# Enter the target number: 6
# The target 6 meets when adding 1 and 5.
# The target 6 meets when adding 2 and 4.
