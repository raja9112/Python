# hex_to_binary

def hex_to_binary(n):


    hex_to_bin_map = {
        '0': "0000", '1': "0001", '2': "0010", '3': "0011",
        '4': "0100", '5': "0101", '6': "0110", '7': "0111",
        '8': "1000", '9': "1001", 'A': "1010", 'B': "1011",
        'C': "1100", 'D': "1101", 'E': "1110", 'F': "1111"
    }

    binary_res = ''

    for digit in n.upper():
        if digit in hex_to_bin_map:
            binary_res += hex_to_bin_map[digit]
        else: 
            raise ValueError("Invalid value")
        
    return binary_res

print(hex_to_binary("1A3F"))


# Direct conversion using Python

# binary_result = bin(int(hex_number, 16))[2:]  # Convert hex to int, then to binary
# print(f"The binary equivalent of hexadecimal {hex_number} is {binary_result}")