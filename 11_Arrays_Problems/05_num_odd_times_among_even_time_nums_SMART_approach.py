def num_odd_times(nums):
	odd = nums[0]
	for i in range(1, len(nums)):
		odd ^= nums[i]
	return odd

nums = [1, 2, 5, 3, 1, 5, 3]
print(num_odd_times(nums))