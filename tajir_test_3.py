def binary_search(arr,target):
    low = 0
    high = len(arr)-1

    while low<=high:
        mid = (low+high) //2
        mid_val = arr[mid]

        if mid_val == target:
            return mid
        elif mid_val > target:
            high = mid-1
        else:
            low = mid+1
    return -1
arr = [1,2,3,4,5,6,7,8]
result=binary_search(arr,3)
print(result)