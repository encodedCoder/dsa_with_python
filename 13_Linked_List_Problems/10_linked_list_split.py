# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import ceil
class Solution:
    def countListNodes(head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        count = self.countListNodes(root)

        result = []
        while root:
            current_length = ceil(count/k)
            count -= current_length
            k -= 1

            new_list = temp = root
            while current_length-1:
                temp = temp.next
                root = root.next
                current_length -= 1
            root = root.next
            temp.next = None
                    
            result.append(new_list)

        while k:
            result.append(None)
            k -= 1

        return result