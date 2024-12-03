def pair_closest_to_zero(arr):
    arr.sort()
    left, right = 0, len(arr) - 1
    closest_sum = float('inf')
    closest_pair = ()

    while left < right:
        pair_sum = arr[left] + arr[right]
        if abs(pair_sum) < abs(closest_sum):
            closest_sum = pair_sum
            closest_pair = (arr[left], arr[right])

        if pair_sum < 0:
            left += 1
        else:
            right -= 1

    return closest_pair

arr = [-1, 2, -3, 4, -2]
print(pair_closest_to_zero(arr))  # Output: (-1, 2)
