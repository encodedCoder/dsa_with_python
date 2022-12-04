def sort_colors_two_pass_appraoch(nums):
    nums_len = len(nums)

    i = 0
    j = nums_len-1

    while i < j:
        if nums[i] == 0:
            i += 1
        elif nums[j] == 0:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            j -= 1

    j = nums_len-1
    while i < j:
        if nums[i] == 1:
            i += 1
        elif nums[j] == 1:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            j -= 1

def sort_colors_one_pass_appraoch(nums):
    nums_len = len(nums)

    i = 0
    j = nums_len-1

    while i <= j:
        if nums[i] == 2:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            elif nums[j] == 1:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            elif nums[j] == 2:
                j -= 1
        elif nums[i] == 1:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            elif nums[j] == 1:
                k = j-1
                while k > i:
                    if nums[k] == 2:
                        nums[k], nums[j] = nums[j], nums[k]
                    k -= 1
                j -= 1
            elif nums[j] == 2:
                j -= 1
        elif nums[i] == 0:
            i += 1

def sort_colors_counting_method(nums):
    zeroes_count = 0
    ones_count = 0
    twos_count = 0

    for i in range(len(nums)):
        if nums[i] == 0:
            zeroes_count += 1
        elif nums[i] == 1:
            ones_count += 1
        else:
            twos_count += 1

    i = 0
    while zeroes_count:
        nums[i] = 0
        i += 1
        zeroes_count -= 1

    while ones_count:
        nums[i] = 1
        i += 1
        ones_count -= 1

    while twos_count:
        nums[i] = 2
        i += 1
        twos_count -= 1


nums = [2, 2, 1, 0, 2, 0, 1, 2]
nums = [2, 0, 2, 1, 1, 0]
# nums = [1,2,1]
# nums = [1,1,1,1,1,1,1,1,1,2,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1]
sort_colors_counting_method(nums)
print(nums)