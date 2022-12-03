def create_target_array(nums, index):
    n = len(nums)
    target_array = [110] * n
    for i in range(len(nums)):
        if target_array[index[i]] != 110:
            j = index[i]
            while target_array[j] != 110:
                j += 1
            while j > index[i]:
                target_array[j] = target_array[j-1]
                j -= 1
            target_array[index[i]] = nums[i]
        else:
            target_array[index[i]] = nums[i]
    return target_array


nums = [0,1,2,3,4]; index = [0,1,2,2,1]
# nums = [1,2,3,4,0]; index = [0,1,2,3,0]
# nums = [1]; index = [0]
print(create_target_array(nums, index))