class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m and n:
            nums1_copy = nums1[:m-n]
            # print(nums1_copy)
            
            i = 0; j = 0; k = 0
            while j < m-n and k < n:
                if nums1_copy[j] <= nums2[k]:
                    nums1[i] = nums1_copy[j]
                    i += 1
                    j += 1
                else:
                    nums1[i] = nums2[k]
                    i += 1
                    k += 1
            
            while j < m-n:
                nums1[i] = nums1_copy[j]
                i += 1
                j += 1

            while k < n:
                nums1[i] = nums2[k]
                i += 1
                k += 1

nums1 = [1,2,3,0,0,0]; m = 3; nums2 = [2,5,6]; n = 3
print(nums1)
Solution.merge(0, nums1, m+n, nums2, n)
print(nums1)