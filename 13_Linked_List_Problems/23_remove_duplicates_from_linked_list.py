'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
Return the linked list sorted as well.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head and head.next:
            dummyNode = ListNode(0,head)

            prev = dummyNode
            curr = head

            while curr and curr.next:
                while curr.next and curr.val != curr.next.val:
                    prev, curr = curr, curr.next
                if curr.next:
                    prev, curr = curr, curr.next
                    while curr.next and curr.val == curr.next.val:
                        curr = curr.next
                    prev.next = curr.next
                    curr = curr.next
            return head