def find_floor_ceil(arr, target):
    floor_val = None
    ceil_val = None
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val == target:
            # If the middle element is equal to the target value, it is both the floor and the ceiling
            return mid, mid
        elif mid_val < target:
            # Update the floor value and search in the right half
            floor_val = mid_val
            low = mid + 1
        else:
            # Update the ceiling value and search in the left half
            ceil_val = mid_val
            high = mid - 1

    # If the target is not found, return the last encountered floor and ceiling values
    return arr.index(floor_val) if floor_val is not None else None, arr.index(ceil_val) if ceil_val is not None else None
arr = [1, 2, 4, 6, 8, 10]
target = 5
floor_index, ceil_index = find_floor_ceil(arr, target)
print(f"Floor value: {arr[floor_index]} at index {floor_index}")
print(f"Ceiling value: {arr[ceil_index]} at index {ceil_index}")
