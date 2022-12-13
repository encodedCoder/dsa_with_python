# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head and head.next:
            dummyNode = ListNode(101, head)

            prev = dummyNode
            curr = head

            while curr and curr.next:
                while curr.next and curr.val != curr.next.val:
                    prev, curr = curr, curr.next
        
                if curr.next:
                    while curr.next and curr.val == curr.next.val:
                        curr = curr.next
                    if prev.next == head:
                        head = curr.next
                    prev.next = curr.next
                    curr = curr.next
        return head