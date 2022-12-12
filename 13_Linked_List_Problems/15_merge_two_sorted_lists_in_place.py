'''
Write a function that takes two lists, each of which is sorted in increasing order,
and merges the two together into one list which is in increasing order. 
Function should return the new list. 
The new list should be made by splicing together the nodes of the first two lists.
'''
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail

    def insert_at_end(self, data):
        newNode = Node(data)
        if self.head:
            self.tail.next = newNode
            self.tail = newNode
        else:
            self.head = self.tail = newNode

    def print_it(self):
        if self.head:
            temp = self.head
            while temp.next:
                print(temp.data, end=' ')
                temp = temp.next
            print(temp.data)

def merge_two_sorted_lists(head1, head2):
    if not head1:
        return LinkedList(head2)
    elif not head2:
        return LinkedList(head1)

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

    return LinkedList(head)  



a = LinkedList()
for i in [2, 4, 9, 10, 12, 14, 14]:
    a.insert_at_end(i)
a.print_it()

b = LinkedList()
for i in [3, 5, 8, 11, 15, 18]:
    b.insert_at_end(i)
b.print_it()

c = merge_two_sorted_lists(a.head, b.head)
c.print_it()


# lst1_len, lst2_len = [int(ele) for ele in input().split()]
# lst1 = [int(ele) for ele in input().split()]
# lst2 = [int(ele) for ele in input().split()]

# a = LinkedList()
# b = LinkedList()

# for i in range(lst1_len):
#   a.insert_at_end(lst1[i])

# for i in range(lst2_len):
#   b.insert_at_end(lst2[i])

# c = merge_two_sorted_lists(a.head, b.head)
# c.print_it()