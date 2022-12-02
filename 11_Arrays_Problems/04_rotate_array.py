def right_rotate_array(nums, k):
    while k:
        i = len(nums)-1
        temp = nums[-1]
        while i:
            nums[i] = nums[i-1]
            i -= 1
        nums[i] = temp
        k -= 1


# nums = [4, 3, 2, 5, 6]
# right_rotate_array(nums, 2)
# print(nums)

nums = [1,2,3,4,5,6,7]
right_rotate_array(nums, 3)
print(nums)