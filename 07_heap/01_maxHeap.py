class Heap:
    def maxHeapify(self, lst, i, lst_len):
        largest = i
        left  = 2*i+1
        right = 2*i+2

        if left < lst_len and lst[left] > lst[largest]:
            largest = left
        
        if right < lst_len and lst[right] > lst[largest]:
            largest = right
        
        if i != largest:
            lst[i], lst[largest] = lst[largest], lst[i]
            self.maxHeapify(lst, largest, lst_len)

    def buildMaxHeap(self, lst, lst_len):
        for i in range(len(lst)//2 - 1, -1, -1):
            self.maxHeapify(lst, i, lst_len)

    def sort(self, lst, lst_len):
        while lst_len > 0:
            lst[0], lst[lst_len-1] = lst[lst_len-1], lst[0]
            lst_len -= 1
            self.maxHeapify(lst, 0, lst_len)

lst = [16,4,10,14,7,9,3,2,8,1]
lst = [8,6,10,5,9,11,13,12,7]
lst = [4,1,3,2,16,9,10,14,8,7]
heap = Heap()
heap.buildMaxHeap(lst, len(lst))
print(lst)
heap.sort(lst, len(lst))
print(lst)

