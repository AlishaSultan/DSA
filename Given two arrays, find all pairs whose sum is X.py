# Given two arrays, find all pairs whose sum is X. e
# Input:
# arr1] = {1, 2, 4, 5, 7}
# arr2[] = {5, 6, 3, 4, 8}
# X = 9
# Output: 18
# 45
# 54
def sum_pair (arr1,arr2,sum):
    pair = []
    for i in arr1:
        for j in arr2:
            if i+j == sum:
                pair.append((i,j))
    return pair
arr1 = [1, 2, 4, 5, 7]
arr2 = [5, 6, 3, 4, 8]
sum = 9
pair = sum_pair(arr1,arr2,sum)
for results in pair:
    print(results)

