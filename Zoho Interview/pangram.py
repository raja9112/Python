import string

def pangram(s):
    sentence = s.lower()
    alphabets = set(string.ascii_lowercase)
    print(sentence, "\n", alphabets)
    return set(sentence) > alphabets


sentence = "The quick brown fox jumps over the lazy dog"
print(pangram(sentence))  # Output: True