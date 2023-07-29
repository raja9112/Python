# reversal algorithm for array rotation

# Function to reverse arr[] from index start to end
def reversearray(arr, start, end):
    while(start<end):
        temp=arr[start]
        arr[start]= arr[end]
        arr[end]=temp
        start+=1
        end =end-1
        
# function to left rotate arr[] of size n by d