#Two number in array with minimum sum

def minimum_sum(arr):
    min1 = min(arr[0],arr[1])
    #print(min1)
    max1 = max(arr[0],arr[1])
    #print(max1)

    for i in range(2,len(arr)):
        if arr[i] < min1:
            max1 = min1
            min1 = arr[i]
        
        elif arr[i] < max1:
            max1 = arr[i]
    
    return min1,max1


arr = [2,3,4,1,6,7]
result = minimum_sum(arr)
print("The minimum sum of two arrays is: ", result)

