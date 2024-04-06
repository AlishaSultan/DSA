def check_balance (s,pairs):
    result = {}
    for pair in pairs:
        if pair in s:
            result[pair] = "balanced"
        else:
            result[pair] = "unbalanced" 
    return result
s = "{{}}[]))"
pairs = ["()", "{}", "[]"]
print(check_balance(s, pairs))