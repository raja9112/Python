def program(s, t):
    def backtracking(index, current_string):
        # If the current string length is 3, process it
        if len(current_string) == 3:
            res.add(current_string.upper())
            res.add(current_string[:2].upper() + "X")  # Add variation with "X"
            return

        # Ensure we don't go out of bounds
        if index >= len(s):
            return

        # Add the current character and proceed with recursion
        backtracking(index + 1, current_string + s[index])
        backtracking(index + 1, current_string)  # Skip the current character
    
    res = set()
    backtracking(0, "")
    
    # Check if the target airport code matches any generated codes
    if t.upper() in res:
        print(f"{t} can be an Airport code for {s}")
    else:
        print(f"{t} cannot be an Airport code for {s}")


# Test cases
program("hyderabad", "HYD")
program("hyderabad", "HDD")
program("losangeles", "LAX")
program("chennai", "CAN")
program("chennai", "MAA")
program("chennai", "CHX")
