def get_t9_words(digits):
    if not digits:
        return []

    # T9 Mapping
    digit_to_char = {
        '2': 'ABC', '3': 'DEF', '4': 'GHI',
        '5': 'JKL', '6': 'MNO', '7': 'PQRS',
        '8': 'TUV', '9': 'WXYZ'
    }

    result = []

    def backtrack(index, current_word):
        if index == len(digits):
            result.append(current_word)
            return 
        
        letters = digit_to_char[digits[index]]
        for letter in letters:
            backtrack(index+1, current_word + letter)

    backtrack(0, "")
    return result


# Example Usage
digits = "23"
print(get_t9_words(digits))  # Output: ["AD", "AE", "AF", "BD", "BE", "BF", "CD", "CE", "CF"]

digits = "7"
print(get_t9_words(digits))  # Output: ["P", "Q", "R", "S"]
