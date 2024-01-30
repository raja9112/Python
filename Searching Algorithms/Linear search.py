# # Linear Search:
# Linear search, also known as sequential search, is a simple search algorithm 
# that checks every element in a list sequentially until the desired element is found or the end of the list is reached.

def LinearSearch(List, target):
    n = len(List)
    for i in range(n):
        if List[i] == target:
            return True
    return False
    
List = [23,5,6,34,3,2,45,12,6,8,76,98,57]
print(LinearSearch(List, 45))