def missing_number (arr):
    arr = sorted(arr)
    left = 0
    right = len(arr)-1
    mid = 0
    while right>=left:
        mid = (left+right)//2
        if arr[mid]!=mid+1:
            right = mid-1
        else:
            left = mid+1
    return left+1
arr = [3,2,4,6]
result = missing_number(arr)
print(result)