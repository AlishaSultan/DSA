#Find 2nd highest element of array			
arr = [1,2,3,4,5,20,30]
arr.sort(reverse=True)	#descending order
#print(arr)	
#;print(arr[1])

#Second Method

def SecondHighest (arr):
    max_1 = float('-inf')
    max_2 = float('-inf')

    for i in arr:
        if i > max_1:
            max_2 = max_1
            max_1 = i
        elif i > max_2:
            max_2 = i
    return max_2
arr = [1,3,4,5,6,20,30]
result = SecondHighest(arr)
print(result)

