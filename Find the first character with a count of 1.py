def find_first_char (s):
    freq = {}
    for i in s:
        if i in freq:
            freq[i]+=1
        else:
            freq[i] = 1
    for i in s:
        if freq[i] == 1:
            return i
s = "Banana"
result = find_first_char(s)
print(result)