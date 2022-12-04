def unsorted_continuous_subarray(nums):
    nums_len = len(nums)
    
    lower_check_point = None
    comparison_point = None
    lower_bound = None
    upper_bound = None

# find the lower bound of unsorted subarray
    # find lower_check_point
    i = 0
    while i <= nums_len-2:
        if nums[i] > nums[i+1]:
            lower_check_point = i
            comparison_point  = i+1
            break
        i += 1

    # find the real possible contributor for lower bound
    i += 2
    if lower_check_point != None:
        while i < nums_len:
            if nums[lower_check_point] >= nums[i] and nums[i] < nums[comparison_point]:
                comparison_point = i
            i += 1

        # find the actual lower bound
        i = lower_check_point-1
        while i >= 0:
            if nums[comparison_point] >= nums[i]:
                lower_bound = i+1
                break
            i -= 1

        if i == -1:
            lower_bound = 0



# find upper bound of unsorted subarray
    if lower_bound != None:
        # find upper_check_point
        i = nums_len-1
        while i >= 1:
            if nums[i] < nums[i-1]:
                upper_check_point = i
                comparison_point  = i-1
                break
            i -= 1

        # find the possible contributor for upper bound
        i -= 2
        while i >= 0:
            if nums[upper_check_point] <= nums[i] and nums[i] > nums[comparison_point]:
                comparison_point = i
            i -= 1

        # find the actual upper bound
        i = upper_check_point+1
        while i <= nums_len-1:
            if nums[comparison_point] <= nums[i]:
                upper_bound = i-1
                break
            i += 1

        if i == nums_len:
            upper_bound = nums_len-1


    if lower_bound != None:
        # print(lower_bound, upper_bound)
        return len(nums[lower_bound:upper_bound+1])
    else:
        # print(lower_bound, upper_bound)
        return 0


nums = [2,6,4,8,10,9,15]
# nums = [1,2,3,4]
# nums = [1]
# nums = [2,1]
# nums = [1,3,2,3,3]
# nums = [1,3,2,2,2]
# nums = [1,1,5,4,3,8,9]
# nums = [2, 2, 2]
# nums = [1, 2, 3, 6, 2, 1, 8, 9, 10, 11, 12, 5, 19, 20, 21]
# nums = [3,2,3,2,4]
# nums = [2,3,3,2,4]
print(unsorted_continuous_subarray(nums))