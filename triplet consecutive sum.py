def triplet_consecutive_sum (arr):
    max_triplet = float('-inf')
    triplet = []
    for i in range(len(arr) - 2):
        triplet_sum = arr[i]+arr[i+1]+arr[i+2]
        if triplet_sum > max_triplet:
            max_triplet = triplet_sum
            triplet = [arr[i],arr[i+1],arr[i+2]]
    return triplet
arr = [2,3,4,5,6,7,9,3,4]
result = triplet_consecutive_sum(arr)
print(result)