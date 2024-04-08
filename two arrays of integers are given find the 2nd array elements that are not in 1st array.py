#2 arrays of integers are given find the 2nd array elements that are not in 1st array
def find_elements (arr1,arr2):
    first_array = set(arr1)
    missing = []
    for i in arr2:
        if i not in first_array:
            missing.append(i)
    return missing
arr1 = [1,2,3,4,5]
arr2 = [1,2,3,6,7,8]
result = find_elements(arr1,arr2)
print(result)
