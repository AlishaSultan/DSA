#find largest difference in an array only from left to right

def largest_difference (arr):
    if len(arr) < 2:
        return 0
    min_ = arr[0]
    max_ = 0
    for num in arr[1:]:
        max_ = max(max_,num-min_)
        min_ = min(min_,num)
    return max_
arr = [2,9,6,3,5,10,11]
result = largest_difference(arr)
print(result)
