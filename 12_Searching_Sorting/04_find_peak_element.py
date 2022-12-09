def findPeakElement(nums):
    nums_len = len(nums)
    
    if nums_len == 1:
        return 0
    elif nums[0] > nums[1]:
        return 0
    elif nums[-1] > nums[-2]:
        return nums_len-1
    
    for i in range(1, nums_len-1):
        if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
            return i


nums = [1,2,1,3,5,6,4]
nums = [1,2,3,1]
nums = [1]
print(findPeakElement(nums)) 