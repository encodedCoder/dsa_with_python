def sort_0s_1s_2s(nums):
	cur  = 0
	low  = 0
	high = len(nums)-1

	while cur < high:
		if nums[cur] == 0:
			nums[low], nums[cur] = nums[cur], nums[low]
			low += 1
			cur += 1
		elif nums[cur] == 1:
			cur += 1
		else:
			nums[cur], nums[high] = nums[high], nums[cur]
			high -= 1


nums = [1, 0, 1, 0, 2, 1]
sort_0s_1s_2s(nums)
print(nums)