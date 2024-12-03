def sort_odd_even(arr):

    odd_numbers = [i for i in arr if i%2 != 0]
    even_numbers = [i for i in arr if i%2 == 0]

    odd_numbers.sort()
    even_numbers.sort(reverse=True)

    res = []
    odd_idx = 0
    even_idx = 0

    for j in arr:
        if j%2 == 0:
            res.append(even_numbers[even_idx])
            even_idx += 1
        else: 
            res.append(odd_numbers[odd_idx])
            odd_idx += 1

    return res


arr = [5, 2, 3, 8, 1, 4, 7, 6]
print(sort_odd_even(arr))

# [1, 8, 3, 6, 5, 4, 7, 2]

# Explanation:
# Separation of Odd and Even Numbers:
# odd_numbers contains all the odd numbers from the array.
# even_numbers contains all the even numbers from the array.
# Sorting:
# odd_numbers.sort() sorts the odd numbers in ascending order.
# even_numbers.sort(reverse=True) sorts the even numbers in descending order.
# Combining the Results:
# We iterate through the original array and, depending on whether an element is odd or even, we append the next sorted odd or even number to the result list.