import sys
def largest(arr, arr_size):

    # the given array must be more than three so,
    if (arr_size<3):
        print("invalid")

    third=first=second= -sys.maxsize

    for i in range(0,arr_size):
        # if the current element is greater than first
        if (arr[i]>first):
            third=second
            second=first
            first=arr[i]

        # if arr[i] is between first and third then update second
        elif (arr[i]>second):
            third=second
            second=arr[i]

        elif (arr[i]>third):
            third=arr[i]

    print(f"The largest three elements are :{first} {second} {third}")

arr=int(input("How many elements you want enter : "))
store=[]
for x in range(arr):
    store.append(int(input("Enter a number : ")))

n=len(store) #finding length of a given array

largest(store,n)
