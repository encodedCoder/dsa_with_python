class Solution:
    def sortedInsert(self, head, data):
        newNode = Node(data)

        if not head:
            head = newNode
            newNode.next = head
        else:
            if newNode.data <= head.data:
                newNode.next = head
                temp =  head
                while temp.next != head:
                    temp = temp.next
                head = newNode
                temp.next = newNode
            else:
                temp = head
                while temp.next != head and newNode.data > temp.next.data:
                    temp = temp.next
                else:
                    if temp.next == head:
                        temp.next = newNode
                        newNode.next = head
                    else:
                        newNode.next = temp.next
                        temp.next = newNode
        return head