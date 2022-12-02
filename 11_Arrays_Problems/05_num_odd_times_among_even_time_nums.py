def num_odd_time(nums):
	count = [0]*(max(nums)+1)

	for i in range(len(nums)):
		count[nums[i]] += 1

	for i in range(len(count)):
		if count[i] % 2 != 0:
			return i


nums = [5, 7, 2, 7, 5, 2, 5]
print(num_odd_time(nums))

nums = [1, 2, 3, 2, 3, 1, 3]
print(num_odd_time(nums))
