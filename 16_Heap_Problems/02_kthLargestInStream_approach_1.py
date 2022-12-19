# APPROACH - Sorting

# def __init__(self, k: int, nums: List[int]):
# def add(self, val: int) -> int:

class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.nums = nums
        self.nums.sort()

    def add(self, val):
        self.nums.append(val)
        self.nums.sort()
        return self.nums[len(self.nums)-self.k]

items = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

k = items[0][0]
nums = items[0][1]
kthLargest = KthLargest(k, nums)
for i in range(1, len(items)):
    print(kthLargest.add(items[i][0]), end=' ')

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)