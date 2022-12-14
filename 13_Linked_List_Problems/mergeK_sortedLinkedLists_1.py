# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
from math import ceil

class MinHeap:
    def __init__(self, lst):
        self.heapList = lst
        self.heapLen  = len(lst)
        self.buildMinHeap()

    def minHeapify(self, i):
        smallest = i
        leftChild = 2*i+1
        rightChild = 2*i+2

        lst = self.heapList

        if leftChild < self.heapLen and lst[leftChild].val < lst[smallest].val:
            smallest = leftChild

        if rightChild < self.heapLen and lst[rightChild].val < lst[smallest].val:
            smallest = rightChild

        if i != smallest:
            lst[i], lst[smallest] = lst[smallest], lst[i]
            self.minHeapify(smallest)
    def buildMinHeap(self):
        for i in range(self.heapLen//2-1, -1, -1):
            self.minHeapify(i)
    def extractMin(self):
        lst = self.heapList
        lst[0], lst[-1] = lst[-1], lst[0]
        pointer = lst.pop()
        self.heapLen -= 1
        self.minHeapify(0)
        return pointer
    def insertIntoMinHeap(self, val):
        lst = self.heapList
        lst.append(val)
        self.heapLen += 1
        i = self.heapLen-1
        while i > 0:
            parent = ceil(i/2) - 1
            if lst[i].val < lst[parent].val:
                lst[i], lst[parent] = lst[parent], lst[i]
                i = parent
            else:
                break

# def mergeKLists(self, lists: List[ListNode]) -> ListNode:
class Solution:
    def mergeKLists(self, lists):
        if lists != []:
            listsLen = len(lists)
            
            # create tempHeap
            lst = []
            for i in range(listsLen):
                if lists[i]:
                    lst.append(lists[i])

            # create minHeap
            heap = MinHeap(lst)

            if lst:
                # point the newHead to minElement
                newHead = heap.extractMin()
                temp = newHead

                while heap.heapLen:
                    if temp.next:
                        heap.insertIntoMinHeap(temp.next)
                    temp.next = heap.extractMin()
                    temp = temp.next

                return newHead


list1Head = temp = ListNode(1)
temp.next = ListNode(4)
temp = temp.next
temp.next = ListNode(5)

list2Head = temp = ListNode(1)
temp.next = ListNode(3)
temp = temp.next
temp.next = ListNode(4)

list3Head = temp = ListNode(2)
temp.next = ListNode(6)

def printList(head):
    if head:
        while head.next:
            print(head.val, end=' ')
            head = head.next
        print(head.val)

print("List 1: ", end=' '); printList(list1Head);
print("List 2: ", end=' '); printList(list2Head);
print("List 3: ", end=' '); printList(list3Head);

printList(Solution.mergeKLists(0, [list1Head, list2Head, list3Head]))