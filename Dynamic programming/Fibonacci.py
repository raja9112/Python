# Method 1: Memoization (Top - down)
memo = {}
def f(n):
    if n == 0 or n == 1:
        return n
    
    if n not in memo:
        memo[n] = f(n-1) + f(n-2)
    
    return memo[n]
print(f(10))

# Method 2: Tabulation (Bottom - Down)
def f(n):
    table = [0] * (n+1)
    
    table[0], table[1] = 0, 1
    
    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]
    
    return table[n]
print(f(10))