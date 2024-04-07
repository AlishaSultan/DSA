def non_duplicate (arr):
    freq = {}
    for i in arr:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    n_duplicate = []
    for i in arr:
        if freq[i] == 1:
            n_duplicate.append(i)
    return n_duplicate
arr = [1,2,2,2,3,4,4,5]
result = non_duplicate(arr)
print(result)