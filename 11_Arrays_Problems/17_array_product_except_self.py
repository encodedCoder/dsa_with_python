def productExceptSelf(nums):
    nums_len = len(nums)

    output_lst = []

    output_lst.append(1)
    for i in range(1, nums_len):
        output_lst.append(output_lst[i-1] * nums[i-1])

    right_side = 1
    for i in range(nums_len-1, -1, -1):
        output_lst[i] = right_side * output_lst[i]
        right_side *= nums[i]

    return output_lst



nums = [1, 2, 3, 4]
# nums = [4, 5, 1, 8, 2, 10, 6]
print(productExceptSelf(nums))