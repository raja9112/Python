# Check if pair with given Sum exists in Array (Two Sum) using hash method
def Sum(arr, target):
    hash_table = {}
    for element in arr:
        hash_table[element] = True
        
    complement = target - element 
    if complement in hash_table:
        return True
    return False

usr = int(input("How many elements do you want add? "))
arr=[]
for i in range(usr):
    arr.append(int(input(f"Enter element {i}: ")))
    
target = int(input("Enter the target number: "))
    
print(Sum(arr, target))

# complement (the number needed to reach the target sum) for each element. 
# If the complement exists in the hash table, it means there's a pair that sums up to the target and returns True.
# arr=[1,2,3,4,5,6]
# target = 7
# complement = 7 - 1 = 6
# 6 is present in arr, so True

# Method 2
# for element in arr:
#     complement = target - element 
#     if complement in hash_table:
#         return True
#     hash_table[element] = True
        
# return False