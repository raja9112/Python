def combinations(k, n):

    def backtrack(index, path, current_sum):

        if len(path) == k and current_sum == n:
            res.append(path[:])

        for i in range(index, 10):
            if current_sum +i <= n:
                backtrack(i + 1, path + [i], current_sum + i)

    res = []
    backtrack(1, [], 0)
    return res


print(combinations(3, 9))