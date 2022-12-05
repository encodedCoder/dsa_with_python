def two_missing_nums(nums):
	nums_len = len(nums)

	total_nums = nums_len+2

	sum2 = (total_nums*(total_nums+1))//2

	sum1 = 0
	for i in range(nums_len):
		sum1 += nums[i]


	two_nums_sum = sum2 - sum1

	for i in range(1, two_nums_sum//2):
		if i not in nums:
			return [i, two_nums_sum-i]

nums = [5, 1, 4, 6, 3]
# nums = [1, 2, 4, 6]
print(two_missing_nums(nums))