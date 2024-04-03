def merge_array(arr1, arr2):
    merge = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merge.append(arr1[i])
            i += 1
        else:
            merge.append(arr2[j])
            j += 1
    while i < len(arr1):
        merge.append(arr1[i])
        i += 1
    while j < len(arr2):
        merge.append(arr2[j])
        j += 1
    return merge

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
result = merge_array(arr1, arr2)
print(result)


#other method:
arr1 = [1,2,3,4,5]
arr2 = [6,7,8,9,10]
arr3 = []
arr3.extend(arr1)
arr3.extend(arr2)
print(arr3)

# Example usage:
def merge_sorted_arrays(arr1, arr2):
    return sorted(arr1 + arr2)
arr1 = [1, 3, 5, 7, 9]
arr2 = [2, 4, 6, 8, 10]
merged_array = merge_sorted_arrays(arr1, arr2)
print(merged_array)


