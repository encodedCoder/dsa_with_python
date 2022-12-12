from math import ceil

class Node:
    def __init__(self, data, next = None):
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
            self.tail      = newNode
            self.tail.next = self.head
        else:
            self.head = self.tail = newNode
            self.tail.next = self.head
    def print_it(self):
        temp = self.head
        while temp.next != self.head:
            print(temp.data, end=', ')
            temp = temp.next
        print(temp.data)
    def count_nodes(self):
        temp = self.head; count = 1
        while temp.next != self.head:
            count += 1
            temp = temp.next
        return count
    def split_into_two_TWO_PASS_APPROACH(self):
        list_length = self.count_nodes()
        
        if list_length >= 2:
            list_1_length = ceil(list_length/2)

            h1 = temp = self.head
            while list_1_length-1:
                temp = temp.next
                list_1_length -= 1
            else:
                t = temp
                temp = temp.next
                t.next = h1
            head1 = LinkedList(h1, t)

            h2 = temp
            while temp.next != h1:
                temp = temp.next
            else:
                temp.next = h2
            head2 = LinkedList(h2, temp)

            return head1, head2
    def split_into_two_ONE_PASS_APPROACH(self):
        if self.head != self.tail:
            slow = fast = self.head
            h1 = self.head

            while self.head not in [fast.next, fast.next.next]:
                fast = fast.next.next
                slow = slow.next
            else:
                t1 = slow
                h2 = slow.next
                slow.next = h1

                if fast.next == self.head:
                    t2 = fast
                else:
                    t2 = fast.next
                t2.next = h2

            return LinkedList(h1, t1), LinkedList(h2, t2)

a = LinkedList()
for i in range(11, 20):
    a.insert_at_end(i)
a.print_it()

x, y = a.split_into_two_ONE_PASS_APPROACH()

x.print_it()
y.print_it()

print(x.head, x.tail.next)
print(y.head, y.tail.next)

a.print_it()