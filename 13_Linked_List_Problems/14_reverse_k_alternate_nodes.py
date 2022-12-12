from pdb import set_trace
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
            self.tail = newNode
        else:
            self.head = self.tail = newNode
    def print_it(self):
        if self.head:
            temp = self.head
            while temp.next:
                print(temp.data, end=', ')
                temp =  temp.next
            print(temp.data)
    def reverse_K_alternate_nodes(self, k):
        if self.head and self.head.next:

        # first adjust the new head
            t = t1 = self.head
            t2 = t1.next
            t3 = t2.next
            i = k-2
            while i and t3:
                t2.next = t1
                t1, t2, t3 = t2, t3, t3.next
                i -= 1
                # set_trace()
            else:
                t2.next = t1
                t.next  = t3
                self.head = t2

        # now reverse the rest list
            temp = t3
            while temp:
                i = k-1
                while i and temp:
                    temp = temp.next
                    i -= 1
                if temp:
                    t = t1 = temp.next
                    if t1:
                        t2 = t1.next
                        if t2:
                            t3 = t2.next
                            i = k-2
                            while i and t3:
                                t2.next = t1
                                t1, t2, t3 = t2, t3, t3.next
                                i -= 1
                            else:
                                t2.next = t1
                                temp.next  = t2
                                t.next = t3
                            temp = t3

# first list
a = LinkedList()
for i in range(1, 6):
    a.insert_at_end(i)
print("Original List: ", end = ''); a.print_it()
a.reverse_K_alternate_nodes(3)
print("Reversed List: ", end = ''); a.print_it(); print("Here k: 3")

# second list
print()
b = LinkedList()
for i in range(1, 20):
    b.insert_at_end(i)
print("Original List: ", end = ''); b.print_it()
b.reverse_K_alternate_nodes(4)
print("Reversed List: ", end = ''); b.print_it(); print("Here k: 4")