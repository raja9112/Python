def permute(nums):
    def backtrack(path):
        if len(nums) == len(path):
            res.append(path[:])
            return
        
        for n in nums:
            if n not in path:
                path.append(n)
                backtrack(path)
                path.pop()
    
    res = []
    backtrack([])
    return res

# Test
nums = [1, 2, 3]
print(permute(nums))