# Approach_01 - Simple Sorting

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.numsSorted = False
        

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.numsSorted = False

    def findMedian(self) -> float:
        numsLen = len(self.nums)
        if not self.numsSorted:
            self.nums.sort()
            self.numsSorted = True
        if numsLen % 2 == 1:
            return self.nums[numsLen//2]
        else:
            return avg(self.nums[numsLen//2-1] + self.nums[numsLen//2]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()