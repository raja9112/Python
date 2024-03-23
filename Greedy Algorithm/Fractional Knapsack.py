def fractional_knapsack(capacity, weights, values):
    # Creating a list of tuples contain(weights, values and factional part (v/w))
    
    # And Sorting the list based on the third element of each tuple using lamba function
    items = sorted([(v, w, v/w) for v, w in zip(values, weights)], key = lambda x: x[2], reverse = True)
    
    total_value = 0
    for value, weight, frac in items:
        if capacity == 0:
            return total_value
        
        amount = min(weight, capacity)
        total_value += amount * frac
        capacity -= amount
        
    return total_value

# Example usage:
weights = [2, 3, 5, 7, 1, 4, 1]
values = [10, 5, 15, 7, 6, 18, 3]
capacity = 15
print(fractional_knapsack(capacity, weights, values))  # Output: 54.6
