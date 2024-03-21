# # 0/1 Knapsack problem

# # The Knapsack Problem is a classic optimization problem in computer science and is often used to demonstrate the principles of dynamic programming. There are two main variations: the 0/1 Knapsack Problem and the Unbounded Knapsack Problem. Let's start with the 0/1 Knapsack Problem.

# 0/1 Knapsack Problem:
# In the 0/1 Knapsack Problem, we are given a set of items, each with a weight 
# and a value, and a knapsack with a maximum weight capacity W. The goal is to maximize the total value of the items in the knapsack without exceeding its capacity.

# def knapsack(weights, values, capacity):
#     n = len(weights)
    
#     dp = [[0] * (capacity + 1) for _ in range(n+1)]
    
#     for i in range(1, n+1):
#         for j in range(1, capacity + 1):
#             if weights[i-1] <= j:
#                 dp[i][j] = max(dp[i-1][j],  values[i-1] + dp[i-1][j - weights[i-1]])
#             else:
#                 dp[i][j] = dp[i-1][j]
                
#     return dp[n][capacity]

# # Example usage:
# values = [1, 2, 5, 6]
# weights = [2, 3, 4, 5]
# capacity = 8
# print(knapsack(weights, values, capacity))  # Output: 8



# To know which values are needed to meet the capacity requirements
def knapsack(weights, values, capacity):
    n = len(weights)
    
    dp = [[0] * (capacity + 1) for _ in range(n+1)]  # Table to compute
    
    included = [[0] * (capacity + 1) for _ in range(n+1)]  # To find which items are included to meet the capacity
    
    for i in range(1, n+1):
        for j in range(1, capacity + 1):
            if weights[i-1] <= j:
                dp[i][j] = max(dp[i-1][j],  values[i-1] + dp[i-1][j - weights[i-1]])
                
                # If current item can be included, update "included" array
                if dp[i-1][j] <  values[i-1] + dp[i-1][j - weights[i-1]]:
                    included[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j]
                
                
    # Backtracking method to find the items included in "included" array
    list_included = []
    j = capacity
    for i in range(n, 0, -1):
        if included[i][j] == 1:
            list_included.append(i)
            j -= weights[i-1]
                
    return dp[n][capacity], list_included

# Example usage:
values = [1, 2, 5, 6]
weights = [2, 3, 4, 5]
capacity = 8
answer, items = knapsack(weights, values, capacity) 

print("Maximum value: ", answer) # 8
print("Items included: ", items) # [4, 2]


