def max_valid_braces (s):
    stack = []
    max_num = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        elif s[i] == ')':
            if stack and s[stack[-1]] == '(':
                stack.pop()
                max_num = max(max_num,i-(stack[-1] if stack else -1))
            else:
                stack.append(i)
    return max_num
s = '((()()())))'
result = max_valid_braces(s)
print(result)