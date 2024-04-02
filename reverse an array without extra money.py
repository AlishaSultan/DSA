#reverse an array without extra money

array = [1,2,3,4,5]
reverse_array = array[::-1]
print(reverse_array)

#Reverse array using two pointer approach

def Two_pointer_approach (arr):
    size = len(arr)
    left = 0
    right = size-1
    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left = left +1
        right = right-1
arr = [1,2,3,4,5,6,7]
result = Two_pointer_approach(arr)
print(result)