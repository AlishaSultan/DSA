# Move Zeroes in left
def shift_left(arr):
    size = len(arr)
    left = 0
    right = size - 1
    while left <= right:
        if arr[left] == 0:
            arr[left], arr[right] = arr[right], arr[left]
            right -= 1
        else:
            left += 1
    return arr

arr = [0, 2, 6, 0, -9, 0, 4, 0, -1]
shifted_array = shift_left(arr)
print(shifted_array)
