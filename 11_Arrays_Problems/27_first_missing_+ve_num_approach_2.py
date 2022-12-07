def firstMissingPositive(nums):
    nums_len = len(nums)
    
    if 1 not in nums:
        return 1
    
    for i in range(nums_len):
        if nums[i] > nums_len or nums[i] <= 0:
            nums[i] = 1

    for i in range(nums_len):
        if nums[abs(nums[i])-1] > 0:
            nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]
    
    print(nums)
    for i in range(1, nums_len):
        if nums[i] > 0:
            return i+1

    return i+2


nums = [1,2,0]
nums = [3,4,-1,1]
nums = [7,8,9,11,12]
nums = []
nums = [0]
nums = [-1, 0, -6, -7]
nums = [0,2,2,1,1]
nums = [3, 4, -1, -2, 1, 5, 16, 0, 2, 0]
nums = [4, 5, 6, 1, 2, 3]
print(firstMissingPositive(nums))