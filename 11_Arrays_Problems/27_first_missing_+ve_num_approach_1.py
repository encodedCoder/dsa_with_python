def firstMissingPositive(nums):
    nums_len = len(nums)
    nums.sort()

    if nums_len == 0:
        return 1

    for i in range(nums_len):
        if nums[i] >= 1:
            break
    
    if nums[i] == 1:
        while i < nums_len-1:
            if nums[i] == nums[i+1]:
                i += 1
            elif nums[i+1] != nums[i]+1:
                return nums[i]+1
            else:
                i += 1
    else:
        return 1

    return nums[i]+1


nums = [1,2,0]
# nums = [3,4,-1,1]
# nums = [7,8,9,11,12]
# nums = []
# nums = [0]
# nums = [-1, 0, -6, -7]
nums = [0,2,2,1,1]
print(firstMissingPositive(nums))