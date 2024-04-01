#Two number in array with minimum sum

def Min_sum (arr):
    min_ = min(arr[0],arr[1])
    max_ = max(arr[0],arr[1])
    for i in range(2 , len(arr)):
        if arr[i] < min_:
            max_ = min_
            min_ = arr[i]
        elif arr[i] < max_:
            max_ = arr[i]
        return min_,max_
arr = [1,10,5,7,8,9]
result = Min_sum(arr)
print(result)
