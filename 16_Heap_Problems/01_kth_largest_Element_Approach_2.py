# using maxHeap
# def findKthLargest(self, nums: List[int], k: int) -> int:

class MaxHeap:
	def __init__(self, lst):
		self.heapList = lst
		self.heapLen  = len(self.heapList)
		# buildMax heap
		for i in range(self.heapLen//2-1, -1, -1):
			self.maxHeapify(i)

	def maxHeapify(self, i):
		biggest = i
		left = 2*i+1
		right = 2*i+2
		
		if left < self.heapLen and self.heapList[left] > self.heapList[biggest]:
			biggest = left

		if right < self.heapLen and self.heapList[right] > self.heapList[biggest]:
			biggest = right

		if biggest != i:
			self.heapList[i], self.heapList[biggest] = self.heapList[biggest], self.heapList[i]
			self.maxHeapify(biggest)

	def extractMax(self):
		self.heapList[0], self.heapList[-1] = self.heapList[-1], self.heapList[0]
		val = self.heapList.pop()
		self.heapLen -= 1
		self.maxHeapify(0)
		return val

class Solution:
    def findKthLargest(self, nums, k):
        maxHeap = MaxHeap(nums)
        for i in range(k-1):
        	maxHeap.extractMax()

        return maxHeap.extractMax()

nums = [13,12,11,14,15,17,18,20,19,16]
print(Solution.findKthLargest(0, nums, 4))