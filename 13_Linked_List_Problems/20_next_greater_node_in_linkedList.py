# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Stack:
    def __init__(self, top = None):
        self.top = top
        pass
    def push(self, val):
        newNode = ListNode(val)
        if self.top:
            newNode.next = self.top
            self.top = newNode
        else:
            self.top = newNode
    def pop(self):
        if self.top:
            t, tVal = self.top, self.top.val
            self.top = self.top.next
            del t
            return tVal
        else:
            print("Empty Stack")
    def print_stack(self):
        if self.top:
            temp = self.top
            while temp.next:
                print(temp.val, end = " ")
                temp = temp.next
            print(temp.val)
        else:
            print("Empty Stack, nothing to print")
class Solution:
    def reverseList(self, head):
        if head and head.next:
            p = head
            c = p.next
            n = c.next

            while n:
                c.next = p
                p, c, n = c, n, n.next
            else:
                c.next = p
                head.next = n
                head = c
        return head
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        head = self.reverseList(head)
        stack = Stack()

        result = []
        while head:
            if not stack.top:
                result.append(0)
            elif stack.top.val > head.val:
                result.append(stack.top.val)
            else:
                while stack.top and stack.top.val <= head.val:
                    stack.pop()
                else:
                    if not stack.top:
                        result.append(0)
                    else:
                        result.append(stack.top.val)

            stack.push(head.val)
            head = head.next
        result.reverse()
        return result