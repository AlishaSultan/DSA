def f(n):
    if n==1:
        return 0
    if n<1:
        return 1
    return n*f(n-1)
result = f(4)
print(result)