def find_max(nums):
    max_num = float("-inf")
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num
nums = [1,4,6,7,9,8,10]
result = find_max(nums)
print(result)