def two_missing_nums(nums):
	nums_len = len(nums)

	xor = 0
	for i in range(nums_len):
		xor ^= nums[i]

	for i in range(1, nums_len+3):
		xor ^= i

	shifting_1 = 1
	while True:
		if (xor & shifting_1) != 0:
			break
		shifting_1 <<= 1


	num1 = 0
	for i in range(nums_len):
		if nums[i] & shifting_1:
			num1 ^= nums[i]

	for i in range(1, nums_len+3):
		if i & shifting_1:
			num1 ^= i

	num2 = xor ^ num1


	return num1, num2

nums = [5, 1, 4, 6, 3]
nums = [1, 2, 4, 6]
nums = [1]
print(two_missing_nums(nums))
