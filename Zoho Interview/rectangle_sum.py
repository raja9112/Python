def rectangle_sum(matrix, r1, c1, r2, c2):
    # Validate indices
    if r1 < 0 or r2 >= len(matrix) or c1 < 0 or c2 >= len(matrix[0]):
        print("Invalid Matrix")
        return
    
    rectangle = []
    total_sum = 0

    for i in range(r1, r2+1):
        row = matrix[i][c1:c2+1]
        rectangle.append(row)
        total_sum += sum(row)

    print("Rectangle:")
    for row in rectangle:
        print(row)

    print(f"Total sum of give indices rectangle: {total_sum}")


# Example Usage
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# Top-left index (1, 1), Bottom-right index (2, 2)
rectangle_sum(matrix, 1, 1, 2, 2)

# Top-left index (0, 0), Bottom-right index (3, 3)
rectangle_sum(matrix, 0, 0, 3, 3)
