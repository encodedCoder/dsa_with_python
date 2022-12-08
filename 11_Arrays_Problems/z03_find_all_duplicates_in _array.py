def findDuplicates(nums):
	nums.sort()

	return set([nums[i] for i in range(len(nums)-1) if nums[i] == nums[i+1]])

nums = [4,3,2,7,8,2,3,1]
print(findDuplicates(nums))