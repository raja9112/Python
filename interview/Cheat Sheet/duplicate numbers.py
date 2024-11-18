arr = [1, 2, 3, 4, 3, 2, 1]

# res = set()
# for i in arr:
#     if i not in res:
#         res.add(i)

# print(res)


# Without using Built in function
def duplicate(arr):
    res = []
    for i in arr:
        is_duplicate = False

        for j in res:
            if i == j:
                is_duplicate = True
                break

        if not is_duplicate:
            res.append(i)
    return res

print(duplicate(arr))