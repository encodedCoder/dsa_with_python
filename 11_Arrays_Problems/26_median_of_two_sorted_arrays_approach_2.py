def findMedianSortedArrays(nums1, nums2):
        nums1_len = len(nums1)
        nums2_len = len(nums2)

    # if either list is empty
        if nums1_len == 0:
            mid = nums2_len//2
            if nums2_len%2 == 1:
                return nums2[mid]
            else:
                return (nums2[mid-1] + nums2[mid]) / 2
        elif nums2_len == 0:
            mid = nums1_len//2
            if nums1_len%2 == 1:
                return nums1[nums1_len//2]
            else:
                return (nums1[mid-1] + nums1[mid]) / 2 

    # if both non-empty
        required_len = nums1_len + nums2_len
        required_mid = (required_len // 2) + 1

        i = j = 0
        result = None
        # if lists cummulative length is odd
        if required_len % 2 == 1:
            while i < nums1_len and j < nums2_len and required_mid:
                    if nums1[i] <= nums2[j]:
                        result = nums1[i]
                        i += 1
                    else:
                        result = nums2[j]
                        j += 1
                    required_mid -= 1
            while required_mid and i < nums1_len:
                result = nums1[i]
                i += 1
                required_mid -= 1
            while required_mid and j < nums2_len:
                result = nums2[j]
                j += 1
                required_mid -= 1

            return result
        # if lists cummulative length is even
        else:
            mid_1 = None
            mid_2 = None
            required_mid -= 1
            while i < nums1_len-1 and j < nums2_len-1 and required_mid:
                    if nums1[i] <= nums2[j]:
                        mid_1 = nums1[i]
                        mid_2 = min(nums1[i+1], nums2[j])
                        i += 1
                    else:
                        mid_1 = nums2[j]
                        mid_2 = min(nums1[i], nums2[j+1])
                        j += 1
                    required_mid -= 1
            while required_mid and i < nums1_len-1:
                mid_1 = nums1[i]
                mid_2 = min(nums1[i+1], nums2[j+1])
                i += 1
                required_mid -= 1
            while required_mid and j < nums2_len:
                mid_1 = nums2[j]
                mid_2 = min(nums1[i-1], nums2[j+1])
                j += 1
                required_mid -= 1

            return (mid_1 + mid_2)/2



# nums1 = [1,3]; nums2 = [2]

nums1 = [1,2]; nums2 = [3,4]

# nums1 = [1,3,10,11]; nums2 = [4,5,7]

# nums1 = [1,2,5]; nums2 = [3,4,8]

# nums1 = [0,0]; nums2 = [0,0]

# nums1 = []; nums2 = [1]

# nums1 = [2]; nums2 = []

# nums1 = [1,2]; nums2 = []

# nums1 = [1,3,5,6,7,8,9,11]; nums2 = [1,4,6,8,12,14,15,17]

print(findMedianSortedArrays(nums1, nums2))