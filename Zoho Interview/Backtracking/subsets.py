def subsets(nums):

    def backtrack(index, path):
        res.append(path[:])

        for i in range(index, len(nums)):
            path.append(nums[i])
            # print(path)
            backtrack(i + 1, path)          # index + 1 will allow duplicate values
            path.pop()
            # print(path)

    res = []
    backtrack(0, [])
    return res

# Test
nums = [1, 2, 3]
print(subsets(nums))