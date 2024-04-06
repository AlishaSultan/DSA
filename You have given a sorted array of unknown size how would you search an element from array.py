#You have given a sorted array of unknown size how would you search an element from array
def binary_search(arr, target):
    left = 0
    right = len(arr)-1
    while right > left:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return -1
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]  # Sorted array
target = 11
print(binary_search(arr, target))