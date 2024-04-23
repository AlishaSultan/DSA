def one_d (arr):
    one_d = []
    stack = arr[::-1]
    while stack:
        current = stack.pop()
        if isinstance(current,list):
            stack.extend(current[::-1])
        else:
            one_d.append(current)
    return one_d
arr = [[2,3,4,5],[2,3],[1]]
result = one_d(arr)
print(result)