#find all non repeating elements from array 0(n)
def non_repeating (arr):
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num]+=1
        else:
            frequency[num]=1
    non_repeat = []
    for num in arr:
        if frequency[num] == 1:
            non_repeat.append(num)
    return non_repeat
arr = [1,2,2,3,3,3,4,5,6,6,6,7,7,8,8,9]
result = non_repeating(arr)
print(result)