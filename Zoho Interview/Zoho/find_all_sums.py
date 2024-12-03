def find_all_sums(n):
    res = []

    def backtrack(start, current_sum, current_num):
        if current_sum == n:
            res.append("+".join(map(str, current_num)))
            return
        
        for i in range(start, n):
            if current_sum + i <= n:
                backtrack(i+1, current_sum + i, current_num + [i])

    backtrack(1, 0, [])
    return res


# Test case
print(find_all_sums(10))
