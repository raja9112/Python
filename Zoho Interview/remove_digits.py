def remove_digits(numbers, digits):
    for d in digits:
        new_numbers = []
        for num in numbers:
            # Remove the digit if it exists in the number
            updated_num = str(num).replace(str(d), '')
            if updated_num:  # Skip empty results
                new_numbers.append(int(updated_num))
        numbers = new_numbers
        print(f"After processing digit {d}: {numbers}")
    return numbers

# Example Usage
numbers = [123, 456, 789, 321]
digits = [2, 3, 1, 5]
print(remove_digits(numbers, digits))
