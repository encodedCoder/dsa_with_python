# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp_head = head
        if head:
            # when we want to remove last node itself
            if n == 1:
                if temp_head.next:
                    while temp_head.next.next:
                        temp_head = temp_head.next
                    else:
                        temp = temp_head.next
                        temp_head.next = None
                        del temp
                else:
                    head = None
                    del temp_head
            # when we want to remove nth node for last where n > 1
            else:
                node_count = 1
                
                first_pointer  = head
                second_pointer = head
                
                while first_pointer.next and node_count <= n:
                    first_pointer = first_pointer.next
                    node_count += 1

                # when target node is first node
                if first_pointer.next == None and node_count == n:
                    head = head.next
                    del second_pointer

                # when target node is inbetween node
                else:
                    while first_pointer.next:
                        first_pointer  = first_pointer.next
                        second_pointer = second_pointer.next
                    else:
                        temp = second_pointer.next
                        second_pointer.next = second_pointer.next.next
                        del temp
        return head