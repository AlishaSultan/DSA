# return sum of even number in an array
def even_number (arr):
    even_sum = 0
    for i in arr:
        if i%2 ==0:
            even_sum+=i
    return even_sum
arr = [1,2,4,6,8,10]
result = even_number(arr)
print(result)

