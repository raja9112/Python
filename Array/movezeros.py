# Time Complexity: O(N), where N is the size of elements of the input array.
# Auxiliary Space: O(1) 

#  Code for move all the zeros to the end of array

def movezeros(arr):
    n=len(arr)
    j=0

    for k in range(n):
        if arr[k] != 0:
            arr[j], arr[k] = arr[k], arr[j]
            j+=1

    print(f"The answer is {arr}")

Input= int(input("How many numbers you want add : "))
arr=[]

for i in range(Input):
    arr.append(int(input(f"Enter number {i} : ")))

movezeros(arr)