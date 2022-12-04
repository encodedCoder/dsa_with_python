def sort_colors(nums):
    current = low = 0
    high = len(nums)-1

    while current <= high:
        if nums[current] == 0:
            nums[low], nums[current] = nums[current], nums[low]
            current += 1
            low += 1
        elif nums[current] == 1:
            current += 1
        elif nums[current] == 2:
            nums[high], nums[current] = nums[current], nums[high]
            high -= 1

nums = [2, 2, 1, 0, 2, 0, 1, 2]
# nums = [2, 0, 2, 1, 1, 0]
# nums = [1,2,1]
# nums = [1,1,1,1,1,1,1,1,1,2,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1]
nums = [2,0,1]
sort_colors(nums)
print(nums)