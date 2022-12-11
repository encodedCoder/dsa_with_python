# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from math import ceil

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        head_1 = head
    # count elements of list
        temp = head
        count = 0
        while temp:
            count += 1
            temp = temp.next

    # if list has one or two or three nodes
        if count == 1:
            return True
        elif count == 2:
            if head.val == head.next.val:
                return True
            else:
                return False
        elif count == 3:
            if head.val == head.next.next.val:
                return True
            else:
                return False

        mid = ceil(count/2)

    # let's reach the required mid node of list
        temp = head
        for i in range(mid):
            temp = temp.next

        t1 = temp
        t2 = t1.next
        t3 = t2.next
        
        t1.next = None

        while t3:
            t2.next = t1
            t1, t2, t3 = t2, t3, t3.next
        else:
            t2.next = t1
            head_2 = t2
    
    #lets do the plaindrome checking
        for i in range(count - mid):
            if head_1.val == head_2.val:
                head_1 = head_1.next
                head_2 = head_2.next
            else:
                return False

        return True