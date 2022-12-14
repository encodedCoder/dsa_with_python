# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        t1, t2 = l1, l2

        carry = 0
        while t1.next and t2.next:
            a, b = t1.val, t2.val

            c = a + b + carry
            if c > 9:
                t1.val = c%10
                carry  = 1
            else:
                t1.val = c
                carry  = 0

            t1, t2 = t1.next, t2.next

        if t1.next:
            a, b = t1.val, t2.val

            c = a + b + carry
            if c > 9:
                t1.val = c % 10
                carry  = 1
            else:
                t1.val = c
                carry  = 0

            t1 = t1.next
            while t1.next:
                c = t1.val + carry
                if c > 9:
                    t1.val = c % 10
                    carry  = 1
                else:
                    t1.val = c
                    carry  = 0
                t1 = t1.next

            c = t1.val + carry
            if c > 9:
                t1.val = c % 10
                t1.next = ListNode(1)
            else:
                t1.val = c

        elif t2.next:
            a, b = t1.val, t2.val

            c = a + b + carry
            if c > 9:
                t1.val = c % 10
                carry  = 1
            else:
                t1.val = c
                carry  = 0
            
            t1.next = t2.next
            t1 =  t1.next
            while t1.next:
                c = t1.val + carry
                if c > 9:
                    t1.val = c % 10
                    carry  = 1
                else:
                    t1.val = c
                    carry  = 0
                t1 = t1.next

            c = t1.val + carry
            if c > 9:
                t1.val = c % 10
                t1.next = ListNode(1)
            else:
                t1.val = c

        else:
            a, b = t1.val, t2.val

            c = a + b + carry
            if c > 9:
                t1.val = c%10
                t1.next = ListNode(1)
            else:
                t1.val = c

        return l1