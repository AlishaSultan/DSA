def distinct_pair (arr,k):
    pair_set = set()
    distict_pair = []
    for i in range(1,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]*arr[j] == k:
                if (arr[i],arr[j]) not in pair_set and (arr[j],arr[i]) not in pair_set:
                    pair_set.add((arr[i],arr[j]))
                    distict_pair.append((arr[i],arr[j]))
    return distict_pair
arr = [1, 2, 3,3,4, 4, 5, 6]
k = 12
result = distinct_pair(arr,k)
print(result)