# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head.next:
            if head.next.next:
                two_jump_pointer = head.next.next
            else:
                return False
        else:
            return False
        
        one_jump_pointer = head
        
        while one_jump_pointer.data != two_jump_pointer.data:
            if two_jump_pointer.next:
                if two_jump_pointer.next.next:
                    two_jump_pointer = two_jump_pointer.next.next
                    one_jump_pointer = one_jump_pointer.next
                else:
                    return False
            else:
                return False
        else:
            return True