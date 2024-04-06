#Find indxes of 2 numbers whose sum is equal to given number in array O(n)
def find_index (n,target):
    index_ = {}
    for i,num in enumerate(n):
        complement = target - num
        if complement in index_:
            return [index_[complement],i]
        index_[num]=i
    return None
n = [2,7,11,12,13]
target = 9
result = find_index(n,target)
print(result)