# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from queue import PriorityQueue        

# def mergeKLists(self, lists: List[ListNode]) -> ListNode:
class Solution:
    def mergeKLists(self, lists):
        if lists != []:
            pQ = PriorityQueue()

            i = 0
            while i < len(lists):
                curr = lists[i]
                pQ.put((curr.val, curr))
                i += 1
            
            print(pQ.get()[1])

            if pQ.empty():
                return []
            
            # point the newHead to minElement
            newHead = pQ.get()[1]
            print(newHead)
            temp = newHead

            while pQ.empty():
                if temp.next:
                    pQ.put((temp.next.val, temp.next))
                temp.next = pQ.get()[1]
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