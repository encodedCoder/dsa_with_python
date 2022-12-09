def kth_largest_element(nums, k):
    nums.sort()
    return nums[len(nums)-k]

nums = [1, 5, 4, 3, 2, 6]
nums = [13,12,11,14,15,17,18,20,19,16]
print(kth_largest_element(nums, 2))