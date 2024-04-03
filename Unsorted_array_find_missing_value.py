#you have an unsorted array from 1 to 100  with one missing number find one number
def find_missing_number (arr):
    arr = sorted(arr)
    hash = set(arr)
    for i in range(1,len(arr)+1):
        if i not in hash:
            return i
    return arr
arr = [2,1,3,4,5,6]
result = find_missing_number(arr)
print(result)
