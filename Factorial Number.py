#Factorial Numbers:
def Factorial_number(n):
    result = 1
    for i in range(1,n+1):
        result*=i
    return result
n = 5
result=Factorial_number(5)
print(result)
 