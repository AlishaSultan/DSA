#product of array except itself
def except_product (arr):
    totalProduct = 1
    for i in arr:
        totalProduct*=i
    product_ex=[]
    for i in arr:
        product_ex.append(totalProduct//i)
    return product_ex
arr = [1,2,3,4]
result = except_product(arr)
print(result)