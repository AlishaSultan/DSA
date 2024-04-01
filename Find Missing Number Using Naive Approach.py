def FindMissingNumber (arr):
    
    n = len(arr)+1
    hash = set(arr)

    for i in range(1,n):
        if i not in hash:
            return i
    return n


arr = [1,2,3,4,6,7,8]
result = FindMissingNumber(arr)
print(result)


 