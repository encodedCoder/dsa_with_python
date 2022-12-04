def increasingTriplet(nums):
    min_index = 0

    low = None
    mid = None

    for i in range(1, len(nums)):
        if nums[i] == nums[min_index]:
            continue
        elif nums[i] < nums[min_index]:
            min_index = i
        elif not mid:
            low = min_index
            mid = i
        elif nums[mid] == nums[i]:
            continue
        elif nums[i] < nums[mid]:
            low = min_index
            mid = i
        else:
            print(low, mid, i)
            return True
    else:
        return False


nums = [1,2,3,4,5]
nums = [5,4,3,2,1]
nums = [2,1,5,0,4,6]
nums = [1, 1, 1, 1, 1]
# nums = [1,1,-2,6]
nums = [1,2,2,1]
print(increasingTriplet(nums))
