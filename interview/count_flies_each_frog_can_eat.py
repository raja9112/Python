# Turing Interview Question

# Problem Statement:
# There are several frogs on a line, each with an integer coordinate X[i] representing its position and a tongue of size S[i]. Additionally, there are flies positioned on integer coordinates 
# Y[j]. A frog can eat a fly j if, and only if, the distance between them is less than or equal to the frog's tongue size, i.e., 

# X[i] - Y[j] ≤S[i].

# Your task is to determine, for each frog, how many flies it can eat.

# Input Format:
# X: A list of integers where X[i] represents the position of the i-th frog.
# S: A list of integers where S[i] represents the size of the tongue of the i-th frog.
# Y: A list of integers where Y[i] represents the position of the i-th fly.

# Output Format:
# The function should return a list of integers where the i-th integer represents the number of flies the i-th frog can eat.
# Examples:
# Example 1:

# X = [1, 4, 5]
# S = [2, 3, 5]
# Y = [2, 3, 5]

# Output:
# [2, 3, 3]

# Explanation:

# Frog at position 1 with tongue size 2 can eat flies at positions [2, 3].
# Frog at position 4 with tongue size 3 can eat flies at positions [2, 3, 5].
# Frog at position 5 with tongue size 5 can eat flies at positions [2, 3, 5].


# Example 2:
# Input:
# X = [3]
# S = [5]
# Y = [7, 1, 2, 6, 4, 5, 3, 0, 8]

# Output:
# [9]

# Explanation:

# Frog at position 3 with tongue size 5 can eat all flies at positions [7, 1, 2, 6, 4, 5, 3, 0, 8].
# Constraints:
# Positions X[i], S[i], Y[i] are non-negative integers.
# No two frogs share the same position in the list X.
# 0≤X[i],Y[i]≤10^5
# There may be cases where there are no frogs.


def count_flies_each_frog_can_eat(X, S, Y):
    res = [0] * len(X)
    
    for i in range(len(X)):
        position_of_frog = X[i]
        size_of_tongue = S[i]
        count = 0
        
        for j in Y:
            if abs(position_of_frog - j) <= size_of_tongue:
                count += 1
                
            res[i] = count
    return res   
    
    
    
# X = [1, 4, 5]
# S = [2, 3, 5]
# Y = [2, 3, 5]

X = [3]
S = [5]
Y = [7, 1, 2, 6, 4, 5, 3, 0, 8]
print(count_flies_each_frog_can_eat(X, S, Y))