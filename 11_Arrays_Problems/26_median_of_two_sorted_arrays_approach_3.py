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


# if both lists are non-empty
    i = 0; j = nums1_len-1
    k = 0; l = nums2_len-1

    mid_1 = (i+j) // 2
    mid_2 = (k+l) // 2
    while i <= j and k <= l:
        if nums1[mid] == nums2[mid]:




nums1 = [1,3]; nums2 = [2]

nums1 = [1,2]; nums2 = [3,4]

# nums1 = [0,0]; nums2 = [0,0]

# nums1 = []; nums2 = [1]

nums1 = [2]; nums2 = []

nums1 = [1,2]; nums2 = []

print(findMedianSortedArrays(nums1, nums2))
