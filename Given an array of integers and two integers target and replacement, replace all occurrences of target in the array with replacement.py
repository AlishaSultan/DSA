#Given an array of integers and two integers target and replacement, replace all occurrences of target in the array with replacement
def replace_target (arr,target):
    for i in range(len(arr)):
        if arr[i] == 1:
            arr[i] = target
    return arr   
arr = [1,2,3,4,5,6,7,1,1,1]
target = 9
result = replace_target(arr,target)
print(result)