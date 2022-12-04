def search_in_rotated_sorted_array(nums, target):
    n = len(nums)
    
    left = 0
    right = n-1

    while left <= right:
        # determine the middle index
        middle = (left+right) // 2

        # check if target is equal to middle element
        if nums[middle] == target:
            return middle

        # check if left subarray is sorted
        elif nums[middle] >= nums[left]:
            # check if target may exist inside sorted left subarray
            if nums[left] <= target and target < nums[middle]:
                return binary_search(nums, left, middle-1, target)
            # when target is not part of the sorted left subarray
            else:
                left = middle+1

        # if left subarray is not sorted then right subarray is sorted
        else :
            # check if target may exist inside sorted right subarray
            if nums[middle] < target and target <= nums[right]:
                return binary_search(nums, middle+1, right, target)
            # when target is not part of the sorted right subarray
            else:
                right = middle-1
    return -1



def binary_search(nums, left, right, target):
    while left <= right:
        middle = (left+right) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            right = middle-1
        else:
            left  = middle+1

    return -1

nums = [4,5,6,7,0,1,2]
print(search_in_rotated_sorted_array(nums, 1))
nums = [1]
print(search_in_rotated_sorted_array(nums, 1))
nums = [3, 1]
print(search_in_rotated_sorted_array(nums, 1))