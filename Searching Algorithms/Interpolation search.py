# Interpolation Search:
# Interpolation search is an improvement over binary search, 
# especially when the elements in the list are uniformly distributed. Instead of always dividing the search interval in half, 
# interpolation search estimates the position of the target value based on its value and the values of the endpoints of the interval.

def InterpolationSearch(List, target):
    List.sort()
    print(List)
    
    low = 0
    high = len(List)-1
    
    while low <= high and List[low] <= target <= List[high]:
        mid = low + ((high - low) // (List[high] - List[low])) * (target - List[low])
        
        if List[mid] == target:
            return mid
        elif List[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    
    return False

List = [23,5,6,34,3,2,45,12,6,8,76,98,57]
print(InterpolationSearch(List, 45))

# Advantages:

# Efficiency: Interpolation search can be faster than binary search, especially for large datasets with uniformly distributed values.
# Adaptive: It adapts to the distribution of values in the list, potentially reducing the number of comparisons required.
# Disadvantages:

# Requires Uniform Distribution: Interpolation search performs well when the values in the list are uniformly distributed. If the distribution is skewed, it may not provide significant improvements over binary search.
# Not Always Efficient: In worst-case scenarios, interpolation search may degrade to O(n), especially if the distribution is not uniform.
