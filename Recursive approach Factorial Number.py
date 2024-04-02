def recursive_function (n):
    if n==0:
      return 1
    return n * recursive_function(n-1)
result = recursive_function(5)
print(result)

