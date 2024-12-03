# To form the largest number from an array without using built-in functions like sort(), you can implement a custom sorting algorithm (such as bubble sort or selection sort) based on the concatenation of the numbers.

# Approach without built-in functions:
# Convert to Strings: Convert each number to a string for easy comparison during concatenation.
# Custom Sorting: Compare each pair of numbers by concatenating them in both orders (x + y and y + x). If y + x is greater, swap their positions.
# Concatenate the Sorted List: Once sorted, join the numbers to form the final result.



def compare(x, y):
    return (y+x) > (x+y)


def bubblesort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n-i-1):
            if compare(arr[j], arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]


def largest_number(arr):

    arr = [str(x) for x in arr]
    bubblesort(arr)
    result = ''.join(arr)
    return '0' if result[0] == '0' else result

# Example Usage
print(largest_number([3, 30, 34, 5, 9]))  # Output: "9534330"