# Check if pair with given Sum exists in Array
def Sum(arr, target):
    n = len(arr) 
    
    for i in range(n):
        for j in (i+1, n):
            if (i+j) == target:
                print(f"The target {target} meets when adding {i} and {j}.")
    #             return
    # return 0

usr = int(input("How many elements do you want add? "))
arr=[]
for i in range(usr):
    arr.append(int(input(f"Enter element {i}: ")))
    
target = int(input("Enter the target number: "))
    
Sum(arr, target)