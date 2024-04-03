# 2D to 1D array
def oneD_buildin (arr):
    array = []
    for i in arr:
        array.extend(i)
    return array
arr = [[2,3,4,5,6],[7,8,9,10,11]]
#one_d = oneD_buildin(arr)
#print("1d array: " , one_d)

#Stack
def oneD_buildin (arr):
    array = []
    stack = arr[::-1]
    while stack:
        current = stack.pop()
        if isinstance(current,list):
            stack.extend(current[::-1])
        else:
            array.append(current)
    return array
arr = [[2,3,4,5,6],[7,8,9,10,11]]
one_d = oneD_buildin(arr)
print("1d array: " , one_d)


