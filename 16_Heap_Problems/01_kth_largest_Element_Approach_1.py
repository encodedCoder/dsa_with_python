# using sorting
class Solution:
    def findKthLargest(self, nums, k):
        nums.sort()
        return nums[len(nums)-k]


nums = [13,12,11,14,15,17,18,20,19,16]
print(Solution.findKthLargest(0, nums, 4))