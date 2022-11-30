from math import ceil

class Heap:
    def minHeapify(self, lst, i, lst_len):
        smallest = i
        left  = 2*i+1
        right = 2*i+2

        if left < lst_len and lst[left] < lst[smallest]:
            smallest = left
        
        if right < lst_len and lst[right] < lst[smallest]:
            smallest = right
        
        if i != smallest:
            lst[i], lst[smallest] = lst[smallest], lst[i]
            self.minHeapify(lst, smallest, lst_len)

    def buildMinHeap(self, lst, lst_len):
        for i in range(len(lst)//2 - 1, -1, -1):
            self.minHeapify(lst, i, lst_len)

    def sort(self, lst, lst_len):
        while lst_len > 0:
            lst[0], lst[lst_len-1] = lst[lst_len-1], lst[0]
            lst_len -= 1
            self.minHeapify(lst, 0, lst_len)

    def minElement(self, lst):
        return lst[0]

    def extractMin(self, lst):
        lst[0], lst[-1] =  lst[-1], lst[0]
        val = lst.pop()
        self.minHeapify(lst, 0, len(lst))
        return val

    def insertIntoMinHeap(self, lst, val):
        lst.append(val)

        i = len(lst)-1
        while i > 0:
            parent = ceil(i/2) - 1  
            if lst[parent] > lst[i]:
                lst[parent], lst[i] = lst[i], lst[parent]
                i = parent
            else:
                break


lst = [16,4,10,14,7,9,3,2,8,1]
lst = [8,6,10,5,9,11,13,12,7]
# lst = [4,1,3,2,16,9,10,14,8,7]
heap = Heap()
heap.buildMinHeap(lst, len(lst))
print(lst)
# heap.sort(lst, len(lst))
# print(lst)

# print(heap.minElement(lst))
# print(heap.extractMin(lst))
# print(lst)

heap.insertIntoMinHeap(lst, 3)
print(lst)
