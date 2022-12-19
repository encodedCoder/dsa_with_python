# using modified quickSort i.e. QuickSelect

import random

class Solution:
    def quickSelect(self, nums, low, high, k):
        pivot = random.randint(low, high)
        nums[high], nums[pivot] = nums[pivot], nums[high]
        pivot = high

        i = low-1
        j = low
        while j < high:
            if nums[j] <= nums[pivot]:
                i += 1
                if i != j:
                    nums[i], nums[j] = nums[j], nums[i]
            j += 1
        i += 1
        nums[i], nums[pivot] = nums[pivot], nums[i]

        if i == k:
            return nums[i]
        elif k < i:
            return self.quickSelect(nums, low, i, k)
        else:
            return self.quickSelect(nums, i, high, k)
    def findKthLargest(self, nums, k):
        return self.quickSelect(nums, 0, len(nums)-1, len(nums)-k)

if __name__ == '__main__':
    nums = [13,12,11,14,15,17,18,20,19,16]; k = 4
    nums = [3,2,1,5,6,4]; k = 2
    nums = [3,2,3,1,2,4,5,5,6]; k = 4
    nums = [99,99]; k = 1
    nums = [-1, -1]; k = 1
    solution = Solution()
    print(solution.findKthLargest(nums, k))