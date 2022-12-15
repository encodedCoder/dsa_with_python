class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack   = []
        hashMap = dict()

        i = len(nums2)-1
        while i >= 0:
            if stack == []:
                stack.append(-1)
                hashMap[nums2[i]] = -1
            elif nums2[i] < nums2[i+1]:
                stack.append(nums2[i+1])
                hashMap[nums2[i]] = nums2[i+1]
            elif nums2[i] > nums2[i+1]:
                while stack and nums2[i] > stack[-1]:
                    del stack[-1]
                else:
                    if stack:
                        hashMap[nums2[i]] = stack[-1]
                    else:
                        stack.append(-1)
                        hashMap[nums2[i]] = -1
            i -= 1

        result = []
        for i in nums1:
            result.append(hashMap[i])

        return result