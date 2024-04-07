#Find an object from an array of object and delete it without affecting the order of object in array
def del_obj (arr,target):
    for i,num in enumerate(arr):
        if num == target:
            del arr[i]
    return arr
arr = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}, {'id': 3, 'name': 'Charlie'}]
target = {'id': 2, 'name': 'Bob'}
result = del_obj(arr, target)
print(result)
