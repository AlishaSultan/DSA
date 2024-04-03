#I have an array like
# [2, [2,3], [4,5,[5,6,7,8], [5,4,[7,4]]]]
# it can be like this, multiple sub arrays within an array. make this 1d but you cant use list comprehension or built-in functions. simple loops but don't use too many loops. answer: use recursion
# Code in O(n)

#one method using stack
#one method using recursion

def rec_one_d (arr):
    flatten= []
    def recursive_func (arr):
        for element in arr:
           if isinstance(element,list):
               recursive_func(element)
           else:
               flatten.append(element)
    recursive_func(arr)
    return flatten
arr = [2, [2,3], [4,5,[5,6,7,8], [5,4,[7,4]]]]
one_d = rec_one_d(arr)
print(one_d)
    

