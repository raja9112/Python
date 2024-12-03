def find_palindromes(sentence):
    words = sentence.split()
    res = []

    for word in words:
        if word == word[::-1]:
            res.append(word)

    return res


# Example Usage
sentence = "madam and racecar are palindromes"
print(find_palindromes(sentence))  # Output: ['madam', 'racecar']
