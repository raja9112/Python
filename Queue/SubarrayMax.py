def max_of_subarrays(arr, k):
    n=len(arr)
    result=[]

    for i in range(n-k+1):
        subarray= arr[i: i+k]
        max_number= max(subarray)
        result.append(max_number)

    return result

# Example usage:
arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
result = max_of_subarrays(arr, k)
print(result)  # Output: [3, 3, 5, 5, 6, 7]


"""max_of_subarrays is a function that takes the input array arr and the size of the subarray k.

We calculate the length of the input array n.

We initialize an empty list called result to store the maximum elements from each subarray.

We loop through the input array arr using a range that goes from 0 to n - k. This loop represents the starting index of each subarray.

Within the loop, we extract the subarray of size k using slicing (arr[i:i + k]).

We find the maximum element within the subarray using the max function.

The maximum element is then appended to the result list.

After processing all subarrays, the function returns the result list containing the maximum elements from each subarray.

This code efficiently finds the maximum element in each subarray of size k."""