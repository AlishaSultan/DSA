#You have an array [3,4,6,7,8,2,3,1] and you have a count n such as 4, so shift first 4 elements of array to the left ( at the end of array

arr = [3,4,6,7,8,2,3,1]
n = 4
shifted_array = arr[n:]+arr[:n]
print(shifted_array)