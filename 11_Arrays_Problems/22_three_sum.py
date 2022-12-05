def threeSum(nums):
    nums.sort()

    nums_len = len(nums)

    triplets_lst = []
    for i in range(nums_len-2):
        l = i+1
        r = nums_len-1
        currSum = 0
        while l < r:
            currSum = nums[i] + nums[l] + nums[r]
            if currSum == 0:
                triplets_lst.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
            elif currSum < 0:
                l += 1
            else:
                r -= 1
    return set([tuple(x) for x in triplets_lst])

nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))