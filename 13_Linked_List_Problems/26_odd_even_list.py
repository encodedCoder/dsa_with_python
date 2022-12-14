# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head and head.next and head.next.next:
            t1 = head
            h = t2 = t1.next

            while t2 and t2.next:
                t1.next = t2.next
                t1 = t2.next

                t2.next = t1.next
                t2 = t1.next

            t1.next = h
        return head