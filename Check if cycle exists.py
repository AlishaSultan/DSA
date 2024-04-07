def check_loop (arr):
    n = len(arr)
    current = 0
    visited = set()
    while True:
        if current in visited:
            return True
        if arr[current] == 0 or current == (current+arr[current])%n:
            return False
        visited.add(current)
        current = (current+arr[current])%n
arr = [2,-1,1,2,2]
result = check_loop(arr)
print(result)