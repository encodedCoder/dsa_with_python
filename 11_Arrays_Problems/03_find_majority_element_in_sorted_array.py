def majority_element_Kind_of_naive_approach(nums):
	thresold = (len(nums) // 2) + 1
	
	count = 1
	for i in range(1, len(nums)):
		if nums[i] == nums[i-1]:
			count += 1
			if count >= thresold:
				return nums[i]
		else:
			count = 1
	else:
		return 'None'


def majority_element_smart_approach(nums):
	i = 0
	len_of_nums = len(nums)
	upper_bound = len_of_nums - (len_of_nums // 2 + 1)
	while i <= upper_bound:
		if nums[i] == nums[i + len_of_nums // 2] :
			return nums[i]
		i += 1
	else:
		return None

nums = [1, 1, 2, 2, 2, 2, 2, 3, 5, 6, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
print(majority_element_smart_approach(nums))