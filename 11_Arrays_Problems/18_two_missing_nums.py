def two_missing_nums(nums):
	nums_len = len(nums)

	nums_range = nums_len+2

	dict_1 = {}
	for i in range(nums_len):
		dict_1[nums[i]] = 1

	output_lst = []
	for i in range(1, nums_range+1):
		if dict_1.get(i) == None:
			output_lst.append(i)

	return output_lst



nums = [5, 1, 4, 6, 3]
nums = [1, 2, 4, 6]
print(two_missing_nums(nums))
