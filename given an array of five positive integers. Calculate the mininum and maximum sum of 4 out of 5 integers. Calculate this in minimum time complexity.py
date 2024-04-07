#given an array of five positive integers. Calculate the mininum and maximum sum of 4 out of 5 integers. Calculate this in minimum time complexity
def min_max (arr):
    arr.sort()
    min_ = sum(arr[:4])
    max_ = sum(arr[1:])
    return min_,max_

    
arr = [2,4,5,6,7]
result = min_max(arr)
print(result)