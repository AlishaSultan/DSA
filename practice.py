#Reverse Array two pointer approach
def two_pointer (arr):
    left = 0
    right = len(arr)-1
    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left = left+1
        right = right-1
    return arr
arr = [1,2,3,4,5,6]
result = two_pointer(arr)
print(result)


