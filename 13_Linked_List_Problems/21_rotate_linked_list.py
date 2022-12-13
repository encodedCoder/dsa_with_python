# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def countNodes(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head and head.next and k:
            count = self.countNodes(head)

            t1 = t2 = head
            
            i = 1
            if k < count:
                loopCount = count - k
            elif k >  count:
                loopCount = count - k%count

            while i < loopCount:
                t2 = t2.next
                i += 1
            else:
                head = t2.next
                t2.next = None

                t2 = head
                while t2.next:
                    t2 = t2.next
                else:
                    t2.next = t1

        return head