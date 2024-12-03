def add_digit_to_number(digit, number):
    res = ""
    chars = str(number)
    for i in chars:
        res += str(int(i) + digit)

    return int(res)

digit = 4
number = 2875
print(add_digit_to_number(digit, number))  # Output: 612119