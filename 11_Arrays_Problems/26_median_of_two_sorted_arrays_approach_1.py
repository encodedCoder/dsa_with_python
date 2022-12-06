def findMedianSortedArrays(nums1, nums2):
        nums1_len = len(nums1)
        nums2_len = len(nums2)

        # merge two lists
        i = j = k = 0

        nums = [0] * (nums1_len + nums2_len)

        while i < nums1_len and j < nums2_len:
            if nums1[i] <= nums2[j]:
                nums[k] = nums1[i]
                i += 1
                k += 1
            else:
                nums[k] = nums2[j]
                j += 1
                k += 1

        while i < nums1_len:
            nums[k] = nums1[i]
            i += 1
            k += 1 

        while j < nums2_len:
            nums[k] = nums2[j]
            j += 1
            k += 1  
          
        nums_len = len(nums)
        nums_mid = nums_len // 2
        if nums_len%2 == 1:
            return nums[nums_mid]
        else:
            return (nums[nums_mid-1] + nums[nums_mid]) / 2



nums1 = [1,3];
nums2 = [2]

# nums1 = [1,2]; 
# nums2 = [3,4]

# nums1 = [0,0]; 
# nums2 = [0,0]

# nums1 = []; 
# nums2 = [1]

# nums1 = [2]; 
# nums2 = []

# nums1 = [1,2];
# nums2 = []

nums1 = [1,3,5,6,7,8,9,11]
nums2 = [1,4,6,8,12,14,15,17]

print(findMedianSortedArrays(nums1, nums2))
