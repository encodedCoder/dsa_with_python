def findDuplicates(nums):
    seen_set = set()
    for i in range(len(nums)):
        if nums[abs(nums[i])-1] < 0:
            seen_set.add(abs(nums[i]))
        else:
            nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]

    return seen_set


nums = [4,3,2,7,8,2,3,1]
nums = [1,1,2]
print(findDuplicates(nums))