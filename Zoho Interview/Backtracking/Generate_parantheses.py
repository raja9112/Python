def generate_parentheses(n):

    def backtrack(path, open_count, close_count):
        if len(path) == n*2:
            # res.append("".join(path[:]))
            res.add(path)
            return

        # if open_count < n:
        #     path.append("(")
        #     backtrack(path, open_count + 1, close_count)
        #     path.pop()

        # if close_count < open_count:
        #     path.append(")")
        #     backtrack(path, open_count, close_count + 1)
        #     path.pop() 

        if open_count < n:
            backtrack(path + "(", open_count + 1, close_count)
            backtrack(path, open_count + 1, close_count)

        if close_count < open_count:
            backtrack(path + ")", open_count , close_count+1)
            backtrack(path, open_count , close_count+1)

    res = set()
    backtrack('', 0, 0)
    return list(res)
# Test
n = 3
print(generate_parentheses(n))