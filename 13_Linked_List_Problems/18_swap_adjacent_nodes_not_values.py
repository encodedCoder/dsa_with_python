# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head
            c = p.next
            n = c.next

            t = p
            head = c
            c.next = p

            while n and n.next:
                p, c, n = n, n.next, n.next.next
                t.next = c

                c.next = p
                t = p
            else:
                t.next = n
        return head