def count_decodings(sequence):

    # Time and Space will be O(n)

    # if not sequence or sequence[0] == '0':
    #     return 0

    # n = len(sequence)
    # dp = [0] * (n+1)
    # dp[0], dp[1] = 1, 1

    # for i in range(2, n+1):
    #     if sequence[i-1] != '0':
    #         dp[i] += dp[i-1]

    #     two_digits = int(sequence[i-2:i])
    #     if (10 <= two_digits <= 26):
    #         dp[i] += dp[i-2]

    # return dp[n]


    # Time: O(n) Space O(1)

    if not sequence or sequence[0] == '0':
        return 0
    n = len(sequence)
    prev1, prev2 = 1, 1

    for i in range(2, n+1):
        current = 0
        if sequence[i-1] != '0':
            current += prev1

        two_digits = int(sequence[i-2:i])
        if (10 <= two_digits <= 26):
            current += prev2

        prev2, prev1 = prev1, current

    return prev1


# Example Usage
sequence = "123"
print(count_decodings(sequence))  # Output: 3

sequence = "226"
print(count_decodings(sequence))  # Output: 3

sequence = "06"
print(count_decodings(sequence))  # Output: 0
