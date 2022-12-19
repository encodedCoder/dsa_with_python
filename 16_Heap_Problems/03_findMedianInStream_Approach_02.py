# Approach_02 - Insertion Sort

class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        
    def insert(self):
        numsLen = len(self.nums)
        if numsLen > 1:
            key = self.nums[numsLen-1]
            j = numsLen-2
            while j >= 0 and self.nums[j] > key:
                self.nums[j+1] = self.nums[j]
                j -= 1
            j += 1
            self.nums[j] = key


    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.insert()
        

    def findMedian(self) -> float:
        numsLen = len(self.nums)
        if numsLen % 2 == 1:
            return self.nums[numsLen//2] 
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()