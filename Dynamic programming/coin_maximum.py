# def min_coins(total, coins):
#     if total == 0:
#         answer = total
#     else:
#         answer = float("inf")
#         for coin in coins:
#             subtotal = total - coin
#             if subtotal < 0:
#                 continue
#             answer = min(answer, min_coins(subtotal, coins) + 1) 
        
#     return answer
    
    
    
# print(min_coins(13, [1,4,5])) # 3


# Dynamic programming - 
# def min_coins(total, coins):
#     memo = {}
#     memo[0] = 0
#     for i in range(1, total+1):
#         memo[i] = float("inf")
#         for coin in coins:
#             if i - coin >= 0:
#                 memo[i] = min(memo[i], memo[i-coin] + 1)
            
#     return memo[total] if memo[total] != float("inf") else -1
     
     
# print(min_coins(13, [1,4,5]))  #3


# How many ways we can solve this problem
# See note to computational part
def coin(total: int, coins: list[int]) -> int:
    # Bottom-up approach
    dp = [0] * (total + 1)
    dp[0] = 1
    
    for i in range(1, total + 1):
        for coin in coins:
        
            if i - coin >= 0:
                dp[i] += dp[i-coin]
    
    return dp[total] if dp[total] != 0 else -1
    
print(coin(5, [1, 4, 5])) # 4

