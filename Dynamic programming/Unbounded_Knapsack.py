def unboundedKnapsack(W, n, val, wt):
    dp = [0 for _ in range(W + 1)]
 
    for i in range(W + 1):
        for j in range(n):
            if (wt[j] <= i):
                dp[i] = max(dp[i], dp[i - wt[j]] + val[j])
 
    return dp[W]

# Example usage:
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 8
print(unboundedKnapsack(capacity, len(weights), values, weights))  # Output: 12

# The output of 12 is indeed correct for the given inputs with your function. 
# The optimal solution is to take three items with weight 2 and value 3, for a total weight of 6 and a total value of 9, 
# and one item with weight 2 and value 3, for a total weight of 8 and a total value of 12. 
# This is because in the Unbounded Knapsack problem, we can use an unlimited number of instances of each item