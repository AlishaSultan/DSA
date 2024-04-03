#Flatten a nested array. e.g Input: [1, 2, [3, 4, 5, [6]], 7, 8] Output: [1, 2, 3, 4, 5, 6, 7, 8]
def flatten(arr):
    array = []
    stack = arr[::-1]
    while stack:
        current = stack.pop()
        if isinstance(current,list):
            stack.extend(current[::-1])
        else:
            array.append(current)
    return array
arr = [1, 2, [3, 4, 5, [6]], 7, 8]
one_d = flatten(arr)
#print(one_d)


def flatten_array(arr):
    flatten = []
    def recursive(arr):
        for i in arr:
            if isinstance(i,list):
                recursive(i)
            else:
                flatten.append(i)
        recursive(arr)
        return flatten
arr = [1, 2, [3, 4, 5, [6]], 7, 8]
one_d = flatten(arr)
print(one_d)

