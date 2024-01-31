# Binary Search:
# Binary search is a more efficient search algorithm compared to linear search, 
# especially for sorted lists. It works by repeatedly dividing the search interval in half. 
# At each step, it compares the middle element of the interval with the target value and decides 
# whether to continue searching in the left or right half.

def BinarySearch(list, target):
    List.sort()
    print(List)
    low = 0
    high = len(List) - 1
    
    while low < high:
        mid = (low + high)//2
        
        if List[mid] == target:
            return mid
        elif List[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return False
    

List = [23,5,6,34,3,2,45,12,6,8,76,98,57]
print(BinarySearch(List, 45))

# Advantages:

# Efficiency: Binary search has a time complexity of O(log n), where n is the number of elements in the list. It significantly reduces the number of comparisons compared to linear search, especially for large datasets.
# Works on Sorted Lists: Binary search requires the list to be sorted, but it's highly efficient for sorted lists.
# Disadvantages:

# Requires Sorted Input: The list must be sorted before applying binary search, which might require additional preprocessing if the list is dynamic.
# Not Applicable to Unsorted Lists: It cannot be directly applied to unsorted lists.