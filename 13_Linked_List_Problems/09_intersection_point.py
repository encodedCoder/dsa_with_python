# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        temp_head_1 = headA
        temp_head_2 = headB

        h1 = temp_head_1
        h2 = temp_head_2

        while h1:
            h3 = h2
            while h3:
                if h1 == h3:
                    print("Intersected at '{}'".format(h1.val))
                    return h1
                h3 = h3.next
            h1 = h1.next