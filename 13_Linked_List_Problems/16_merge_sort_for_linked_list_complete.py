class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self, head = None):
        self.head = head
        return None
    def insert_first(self, data):
        newNode = Node(data)
        if self.head:
            newNode.next = self.head
            self.head = newNode
        else:
            self.head = newNode
    def print_it(self):
        if self.head:
            temp = self.head
            while temp.next:
                print(temp.data, end=' ')
                temp = temp.next
            print(temp.data)

    def divide(self, head):
        if head:
            slow = fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            second = slow.next
            slow.next = None
            return second

    def merge_sort(self, head):
        if head and head.next:
            first  = head
            second = self.divide(head)

            first  = self.merge_sort(first)
            second = self.merge_sort(second)

            firstMerged = self.merge(first, second)

            return firstMerged
        else:
            return head

    def merge(self, head1, head2):
        if not head1:
            return head2
        elif not head2:
            return head1

        if head1.data <= head2.data:
            head = head1
            head1 = head1.next
        else:
            head = head2
            head2 = head2.next

        temp = head
        while head1 and head2:
            if head1.data <= head2.data:
                temp.next = head1
                temp = temp.next
                head1 = head1.next
            else:
                temp.next = head2
                temp = temp.next
                head2 = head2.next

        if head1:
            temp.next = head1

        elif head2:
            temp.next = head2

        return head  


a = [5, 4, 8, 6, 7, 2, 9, 1, 3, 2, 4]
a = [8, 1, 2, 4, 3, 1, 6, 5, 4]
a.reverse()

b = LinkedList()
for i in a:
    b.insert_first(i)
b.print_it()
b.head = b.merge_sort(b.head)
b.print_it()