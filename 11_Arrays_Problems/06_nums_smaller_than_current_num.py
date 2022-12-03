def count_smaller_nums(nums):
	lst = []
	for i in range(len(nums)):
		current_num = nums[i]
		count = 0
		for j in range(len(nums)):
			if current_num > nums[j]:
				count += 1
		lst.append(count)
	return lst


nums = [7, 7, 7, 8]
nums = [8,1,2,2,3]
nums = [6,5,4,8]
print(count_smaller_nums(nums))