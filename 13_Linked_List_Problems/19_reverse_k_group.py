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
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head and head.next and k > 1:
            parts = self.countNodes(head) // k

            p = head
            c = p.next
            n = c.next

            t1 = p

        # Adjust new head
            i = k-1
            while i:
                i -= 1
                c.next = p
                p, c = c, n
                if n:
                    n = n.next
            else:
                head = p
                parts -= 1

        # reverse the rest k groups
            while parts:
                i = k-1
                p, c, n = c, c.next, c.next.next
                t2 = p
                while i:
                    c.next = p
                    p, c = c, n
                    if n:
                        n = n.next
                    i -= 1
                else:
                    t1.next = p
                    t1 = t2
                    parts -= 1
            else:
                t1.next = c

        return head