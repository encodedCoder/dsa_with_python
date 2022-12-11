class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_count = 0

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.node_count == 0:
            self.head = self.tail = new_node
            self.node_count += 1
        else:
            temp_head = self.head
            while temp_head != self.tail:
                temp_head = temp_head.next
            self.tail.next = self.tail = new_node
            self.node_count += 1

    def print_it(self):
        if self.node_count == 0:
            print("Empty List")
        else:
            temp_head = self.head
            while temp_head:
                print(temp_head.data, end = ',  ')
                temp_head = temp_head.next
            print("\nTotal Nodes: {}".format(self.node_count))

    # node count approach [Single Traversal Solution]
    def kth_from_last_node_count(self, k):
        temp_count = 1
        temp_head = self.head
        while temp_count <= self.node_count-k:
            temp_head = temp_head.next
            temp_count += 1
        print(temp_head.data)

    # two pointer approach [Single Traversal Solution]
    def kth_from_last_two_pointer(self, k):
        first_pointer = self.head
        i = 1
        while i < k:
            first_pointer = first_pointer.next
            i += 1
        second_pointer = self.head
        while first_pointer.next:
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next
        print(second_pointer.data)


sll = SinglyLinkedList()

sll.insert_at_end(1)
sll.insert_at_end(2)
sll.insert_at_end(3)
sll.insert_at_end(4)
sll.insert_at_end(5)
sll.insert_at_end(6)
sll.insert_at_end(7)

sll.kth_from_last_two_pointer(7)

sll.print_it()
