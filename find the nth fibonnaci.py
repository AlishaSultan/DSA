#find the nth fibonnaci

def fibonnaci (n):
    if n <= 1:
        return n
    else:
        return fibonnaci(n-1)+fibonnaci(n-2)
n = 8
result = fibonnaci(n)
print(result)
