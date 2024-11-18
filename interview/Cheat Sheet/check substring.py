# is_substring

def is_substring(n, m):

    # Keeping sliding window in boundary (len(n)-len(m) + 1)
    for i in range(0, len(n)-len(m) + 1):
        if n[i: i+len(m)] == m:
            return True
    return False

print(is_substring("hello world", "world"))  # True
print(is_substring("hello world", "test"))   # False