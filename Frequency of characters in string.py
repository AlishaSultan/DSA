def frequency_character(string):
    frequency = {}
    for num in string:
        if num in frequency:
            frequency[num]+=1
        else:
            frequency[num]=1
    repeating_elements = {}
    for num, freq in frequency.items():
        if freq > 1:
            repeating_elements[num] = freq
    return repeating_elements
string = ('a','b','b','b','c','c','d','f')
result = frequency_character(string)
print(result)