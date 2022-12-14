# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head
            c = p.next
            n = c.next

            p.next = None
            while n:
                c.next = p
                c, p, n = c, n, n.next
            else:
                c.next = p
                head = c
        return head