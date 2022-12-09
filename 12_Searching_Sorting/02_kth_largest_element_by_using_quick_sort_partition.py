def findKthLargest(nums, k):
    return quick_sort(nums, 0, len(nums)-1, k)


def quick_sort(nums, lower_bound, upper_bound, k):
    index = partition(nums, lower_bound, upper_bound)
    if index == len(nums)-k:
        return nums[index]
    elif index < len(nums)-k:
        if len(nums)-k == index+1:
            return min(nums[index+1:upper_bound+1])
        elif len(nums)-k == upper_bound:
            return max(nums[index+1:upper_bound+1])
        return quick_sort(nums, index+1, upper_bound, k)
    else:
        if len(nums)-k == index-1:
            return max(nums[lower_bound:index])
        elif len(nums)-k == lower_bound:
            return min(nums[lower_bound:index])
        return quick_sort(nums, lower_bound, index-1, k)


def partition(nums, lower_bound, upper_bound):
    pivot = nums[upper_bound]

    i = lower_bound
    j = lower_bound-1

    while i < upper_bound:
        if pivot > nums[i]:
            j += 1
            nums[i], nums[j] = nums[j], nums[i]
        i += 1
    j += 1
    nums[j], nums[upper_bound] = nums[upper_bound], nums[j]

    return j



nums = [6,2,7,1,3,4,5]
nums = [13,12,11,14,15,17,18,20,19,16]
nums = [8,5,3,4]
k = 4
nums = [3,2,1,5,6,4]; k = 2
nums = [3,2,3,1,2,4,5,5,6]; k = 4
print(findKthLargest(nums, k))