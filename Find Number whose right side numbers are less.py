#Find Number whose right side numbers are less

def max_num (arr):
    n = len(arr)
    max_number = arr[n-1]

    for i in range(n-2,-1,-1):
        if arr[i] > max_number:
            return arr[i]
        else:
            max_number=max(arr[i],max_number)
    return -1

arr = [5,7,3,8,2,6]
result = max_num(arr)
print(result)