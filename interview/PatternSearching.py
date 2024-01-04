def pattern_search(text, pattern):
    t_len = len(text)
    p_len = len(pattern)

    # Slide the pattern over the text
    for i in range(t_len - p_len + 1):
        # print(i)
        match = True
        # Check for a match starting from the current index i
        for j in range(p_len):
            # print(text[i+j], pattern[j])
            if text[i + j] != pattern[j]:
                match = False
                break
        # If the match is found, print the index
        if match:
            print(f"Pattern found at index {i}")

# Example usage:
text = "ABCCDDAEFG"
pattern = "CDD"
pattern_search(text, pattern) # 3

# 0
# A C
# 1
# B C
# 2
# C C
# C D
# 3
# C C
# D D
# D D
# Pattern found at index 3
# 4
# D C
# 5
# D C
# 6
# A C
# 7
# E C
