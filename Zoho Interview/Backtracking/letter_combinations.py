def letter_combinations(digits):
    if not digits:
        return None

    phone_map = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }
    
    def backtrack(index, path):
        if index == len(digits):
            res.append(''.join(path))
            return

        for i in phone_map[digits[index]]:
            path.append(i)
            backtrack(index+ 1, path)
            path.pop()

    res = []
    backtrack(0, [])
    return res
    
# Test
digits = "23"
print(letter_combinations(digits))