#given an array string print all possible palindromes
def isPalindrome(arr):
    return arr == arr[::-1]
def find_palindromes(arr):
    palindrome = []
    for word in arr:
        if isPalindrome(word):
            palindrome.append(word)
    return palindrome 
arr = ["abc", "car", "ada", "racecar", "cool"]
print(find_palindromes(arr))
