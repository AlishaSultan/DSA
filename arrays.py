#Array Creation
import array as arr
arr1 = arr.array('i',[1,2,3])
#print(type(arr1))
for i in range(0,3):
    #print("The arrays of integer is: " , arr1[i])
    pass

arr2 = arr.array('d',[3.4,5.6,9.0])
for j in range(0,3):
    #print("The arrays of double is: ",arr2[j])
    pass

#Insertion:
arr1.insert(1,5)
for i in range(0,4):
    #print(arr1[i])
    pass

arr1.append(7)
for i in range(0,5):
    #print(arr1[i])
    pass

#Access the Arrays of Elements
#print(arr1[3])
#print(arr1[0])

#Remove Element from the Array
arr3 = arr.array('i',[1,4,5,7,3,4,1,10])
for i in range(0,7):
    #print(arr3[i])
    pass

arr3.remove(7)
#print(arr3)

#raise error because element is not present in array
#arr3.remove(15)
#print(arr3)
# Traceback (most recent call last):
#   File "e:\Data\DSA\arrays.py", line 39, in <module>
#     arr3.remove(15)
# ValueError: array.remove(x): x not in array

#raise error not deleting more elements 
#arr3.remove(5,7,3)
# Traceback (most recent call last):
#   File "e:\Data\DSA\arrays.py", line 39, in <module>
#     arr3.remove(15)
# ValueError: array.remove(x): x not in array
# PS C:\Users\Alisha>

#Use pop()
#print(arr3)

#print(arr3.pop(2))
#print(arr3)

#Slicing of an array

a = [1,2,3,4,5,6,7,8,9]
array_1= arr.array('i',a)
# print(array_1)
# print(a[3:])
# print(a[:])
# print(a[:-1])

#Searching Elements in an array

# print(array_1)
# print(array_1.index(3))

#Update Elements in an Array

array_1[3] = 10
#print(array_1)

#Python Operations
#Count

# print(array_1)
# print(array_1.count(10))

array_2 = [2,2,4,5,6,7,2,2,2]
arr_2 = arr.array('i',array_2)
# print(arr_2)
# print(arr_2.count(2))

#Reverse Array
# print(arr_2)
# arr_2.reverse()
# print(arr_2)

#Extend

ar = [1,2,3,4,5,6,7]
c = arr.array('i',ar)
print(c)

c.extend([8,9,10])
print(c)





