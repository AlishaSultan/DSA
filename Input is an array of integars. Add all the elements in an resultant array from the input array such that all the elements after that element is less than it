#Input is an array of integars. Add all the elements in an resultant array from the input array such that all the elements after that element is less than it.
def add_elements (arr):
    result = []
    for i in range(len(arr)):
        total = arr[i]
        for j in range(i+1,len(arr)):
            if arr[j] < arr[i]:
                total+=arr[j]
        result.append(total)
    return result
arr = [3, 1, 2, 5, 4, 8, 6]
print(add_elements(arr))  
