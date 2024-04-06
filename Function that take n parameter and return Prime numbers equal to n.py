#Function that take n parameter and return Prime numbers equal to n
def is_Prime_number (n):
    if n <= 1:
        return False
    if n%2==0:
        return False
    return True
def Prime_number(n):
    prime = []
    for i in range(2,n+1):
        if is_Prime_number(i):
            prime.append(i)
    return prime
n = 20
result = Prime_number(n)
print(result)