from math import ceil

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self, head = None, node_count = 0):
        self.head = head
        self.node_count = node_count
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.node_count += 1
    def print_it(self):
        try:
            temp_head = self.head
            while temp_head:
                print(temp_head.data, end=', ')
                temp_head = temp_head.next
            print('\nTotal Nodes: ',self.node_count)
        except AttributeError:
            print("'Most Likely List Does not exist'")
    def insert_at_end(self, data):
        new_node = Node(data)
        temp_head = self.head
        if self.head:
            while temp_head.next:
                temp_head = temp_head.next
            temp_head.next = new_node
        else:
            self.head = new_node
        self.node_count += 1
    def insert_after_position(self, data, position):
        new_node = Node(data)
        if self.head != None:
            temp_head = self.head
            while temp_head.next and position-1:
                temp_head = temp_head.next
                position -= 1
            new_node.next = temp_head.next
            temp_head.next = new_node
        else:
            self.head = new_node
        self.node_count += 1
    def delete_first(self):
        if self.head:
            temp = self.head
            self.head = self.head.next
            del temp
            self.node_count -= 1
    def delete_last(self):
        if self.head:
            temp_head = self.head
            while temp_head.next.next:
                temp_head = temp_head.next
            temp = temp_head.next
            temp_head.next = None
            del temp
            self.node_count -= 1
    def delete_this(self, target_data):
        if self.head:
            temp_head = self.head
            while temp_head.next.data != target_data:
                temp_head = temp_head.next
            temp = temp_head.next
            temp_head.next = temp.next
            del temp
            self.node_count -= 1
    def search(self, target_data):
        if self.head:
            temp_head = self.head
            while temp_head.data != target_data:
                temp_head = temp_head.next
            return temp_head
    def reverse(self):
        if self.node_count > 1:
            t1 = self.head
            t2 = t1.next
            t3 = t2.next

            t1.next = None
            while t3:
                t2.next = t1
                t1, t2, t3 = t2, t3, t3.next
            else:
                t2.next = t1
                self.head = t2
    # split_into_two function is WORK IN PROGRESS
    def split_into_two(self):
        head1 = temp1 = self.head
        head2 = temp2 = self.head.next

        count_1 = count_2 = 1
        while temp1 and temp2:
            temp1.next = temp2.next
            temp1 = temp2.next
            if temp1 and temp1.next:
                count_1 += 1

            temp2.next = temp1.next
            temp2 = temp1.next
            if temp2 and temp2.next:
                count_2 += 1
        else:
            if temp1:
                temp1.next = None
            else:
                temp2.next = None

        del self.head

        return SinglyLinkedList(head1, count_1), SinglyLinkedList(head2, count_2)


lst = SinglyLinkedList()
# 1 2 3 4 5 6 7  
lst.insert_at_end(1)
lst.insert_at_end(2)
lst.insert_at_end(3)
lst.insert_at_end(4)
lst.insert_at_end(5)
lst.insert_at_end(6)
lst.insert_at_end(7)


lst.print_it()
h1, h2 = lst.split_into_two()

h1.print_it()
h2.print_it()

lst.print_it()