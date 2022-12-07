def findPair(nums):
	nums.sort()

	i = 0
	j = len(nums)-1
	sum_ = 100
	while i < j:
		sum_ = min(sum_, nums[i] + nums[j])
		if sum_ < nums[i] + nums[j]:
			j -= 1


nums = [-2, 1, 2, -5, 6, 9]
print(findPair(nums))