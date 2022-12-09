def wiggleSort(nums):

	for i in range(1, len(nums)-1, 2):
		if nums[i] < nums[i-1]:
			nums[i], nums[i-1] = nums[i-1], nums[i]
		if nums[i] < nums[i+1]:
			nums[i], nums[i+1] = nums[i+1], nums[i]


nums = [ 5, 1, 3, 2, 4 ]
wiggleSort(nums)
print(nums)