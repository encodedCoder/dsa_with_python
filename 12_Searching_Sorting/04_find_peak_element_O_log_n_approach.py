def findPeakElement(nums):
        nums_len = len(nums)

        if nums_len == 1:
            return 0

        lower_bound = 0
        upper_bound = nums_len-1

        while lower_bound <= upper_bound:
            mid = (lower_bound + upper_bound) // 2

            if mid == 0:
                if nums[mid] > nums[mid+1]:
                    return mid
                else:
                    return mid+1
            elif mid == nums_len-1:
                if nums[mid] > nums[mid-1]:
                    return mid
                else:
                    return mid-1
                            
            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid
            elif mid > 0 and nums[mid] < nums[mid-1]:
                upper_bound = mid-1
            else:
                lower_bound = mid+1


nums = [1,2,1,3,5,6,4]
# nums = [1,2,3,1]
# nums = [1]
# nums = [1,2]
print(findPeakElement(nums)) 