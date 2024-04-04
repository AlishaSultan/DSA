def Pair_Count (arr,avg):
    pair = []
    count = 0
    for i in range(1,len(arr)):
        for j in range(i+1,len(arr)):
            if (arr[i]+arr[j])//2 == avg:
                pair.append((arr[i],arr[j]))
                count+=1
        return count, pair
arr = [2,1,3]
avg = 2
result = Pair_Count(arr,avg)
print(result)