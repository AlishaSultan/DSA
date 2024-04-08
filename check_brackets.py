def check_brackets (s,pair):
    result = {}
    for pairs in pair:
        if pairs in s:
            result[pairs] ="balanced"
        else:
            result[pairs] = "unbalanced"
    return result
s = "[(){}]"
pair = ["()", "{}", "[]"]
result = check_brackets(s,pair)
print(result)