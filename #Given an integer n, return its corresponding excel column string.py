#Given an integer n, return its corresponding excel column string
def corresponding_excel (n):
    alphabet = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J", 11: "K", 12: "L",
                13: "M", 14: "N", 15: "O", 16: "P", 17: "Q", 18: "R", 19: "S", 20: "T", 21: "U", 22: "V", 23: "W",
                24: "X", 25: "Y", 26: "Z"}
    result = ''
    while n > 0:
        remainder = (n-1)%26
        result = alphabet[remainder+1]+result
        n = (n-1)//26
    return result
testCases = [1,4,44,23,5,6]
for n in testCases:
    print(f"For n={n} => Output: {corresponding_excel(n)}")
