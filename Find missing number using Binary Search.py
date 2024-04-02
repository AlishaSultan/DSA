#Find missing number using Binary Search

def binary_Search (arr,size):
    if arr[0]!=1:
        return 1
    if arr[size-1]!=(size+1):
        return size+1
    left = 0
    right = size -1
    mid = 0
    while right >= left:
        mid = (left+right) // 2
        if arr[mid]!=mid+1:
            right = mid-1
        else:
            left = mid+1
    return left+1
arr = [1,2,3,4,5,6,7]
size = len(arr)
result = binary_Search(arr,size)
print(result)
