def sliding_window (arr,k,target):
    window_size = sum(arr[:k])
    start = 0
    for end in range(k,len(arr)):
        if window_size == target:
            return arr[start:end]
        window_size = window_size-arr[start]+arr[end]
        start+=1
    if window_size == target:
        return arr[start:]
    return []
arr = [2,3,5,6,7,2,4,5,8]
k = 3
target = 17
print(sliding_window(arr,k,target))