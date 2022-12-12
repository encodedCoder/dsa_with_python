"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head:
            temp = head
            while temp:
                new_node  = Node(temp.val, temp.next)
                temp.next = new_node
                temp = new_node.next

            temp = head
            while temp:
                if temp.random:
                    temp.next.random = temp.random.next
                else:
                    temp.next.random = None
                temp = temp.next.next

            t = head
            head = head.next
            temp = head
            del t
            while temp.next:
                t = temp.next
                temp.next = t.next
                temp = temp.next
                del t

            return head