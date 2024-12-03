def combination_sum(candidates, target):

    def backtrack(index, current_sum, path):

        if current_sum == target:
            res.append(path[:])
            return
        
        if current_sum > target:
             return
        
        for i in range(index, len(candidates)): 
                path.append(candidates[i])
                # print(path)
                backtrack(i, current_sum + candidates[i], path)
                path.pop()
                # print(path)


    res = []
    backtrack(0, 0, [])
    return res

# Test
candidates = [2, 3, 6, 7]
target = 7
print(combination_sum(candidates, target))