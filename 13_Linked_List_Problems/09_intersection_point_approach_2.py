# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def compute_list_length(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        list_1_length = self.compute_list_length(headA)
        list_2_length = self.compute_list_length(headB)

        list_1_smaller = False
        list_2_smaller = False
        if list_1_length < list_2_length:
            list_1_smaller = True
        else:
            list_2_smaller = True

        '''
        if both lists are of different sizes make the bigger list 
        reach equivaent to smaller list length
        '''
        h1 = headA
        h2 = headB

        if list_1_smaller:
            for i in range(list_2_length - list_1_length - 1):
                h2 = h2.next
        else:
            for i in range(list_1_length - list_2_length - 1):
                h1 = h1.next

        while h1:
            if h1 == h2:
                return h1
            h1 = h1.next
            h2 = h2.next