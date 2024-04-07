def triplet_consecutive_sum(arr):
    target = 0
    triplets = []
    for i in range(len(arr) - 2):
        triplet_sum = arr[i] + arr[i + 1] + arr[i + 2]
        if triplet_sum == target:
            triplets.append([arr[i], arr[i + 1], arr[i + 2]])
    return triplets
arr = [-3, 2, 0, -5, 1, 5]
result = triplet_consecutive_sum(arr)
print(result)
