class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = None

class CircularSinglyLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_count = 0
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.node_count += 1
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head 
        else:
            temp = self.tail
            self.tail = new_node
            temp.next = new_node
            new_node.next = self.head
        self.node_count += 1
    def print_it(self):
        if self.node_count == 0:
            print("Empty List")
        elif self.node_count == 1:
            print(self.head.data, end=' ')
        else:
            temp_head = self.head
            while temp_head.next != self.head:
                print(temp_head.data, end = ', ')
                temp_head = temp_head.next
            print(temp_head.data)
        print("Total node: {}\n".format(self.node_count))
    def delete_first(self):
        if self.node_count == 0:
            print("Empty List")
        elif self.node_count == 1:
            temp = self.head
            self.head = self.tail = None
            del temp
            self.node_count -= 1
        else:
            temp = self.head
            self.head = self.head.next
            self.tail.next = self.head
            del temp
            self.node_count -= 1
    def delete_last(self):
        if self.node_count == 0:
            print("Empty List")
        elif self.node_count == 1:
            temp = self.head
            self.head = None
            self.tail = None
            del temp
            self.node_count -= 1
        else:
            temp_head = self.head
            while temp_head.next != self.tail:
                temp_head = temp_head.next
            temp = temp_head.next
            self.tail = temp_head
            temp_head.next = self.head
            del temp
            self.node_count -= 1

    def delete_this(self, target_data):
        if self.node_count == 0:
            print("Empty List")
        elif self.node_count == 1 and self.head.data == target_data:
            temp = self.head
            self.head = self.tail = None
            del temp
            self.node_count -= 1
        else:
            # if target node is first node
            if self.tail.next.data == target_data:
                temp = self.head
                self.tail.next = self.head.next
                self.head = temp.next
                del temp
                self.node_count -= 1
            # if target node is last node or in between node
            else:
                temp_head = self.head
                while temp_head.next.data != target_data and temp_head != self.tail:
                    temp_head = temp_head.next
                if temp_head == self.tail:
                    print("Element not present")
                    return
                # when target node is last node
                elif temp_head.next.data == target_data and temp_head.next == self.tail:
                    temp = temp_head.next
                    self.tail = temp_head
                    self.tail.next = self.head
                    del temp
                    self.node_count -= 1
                # when target node is inbetween node
                else:
                    temp = temp_head.next
                    temp_head.next = temp.next
                    del temp
                    self.node_count -= 1

cirSLL = CircularSinglyLL()

cirSLL.insert_at_beginning(4)
cirSLL.insert_at_beginning(8)
cirSLL.insert_at_beginning(54)
cirSLL.insert_at_end(77)
cirSLL.print_it()
# cirSLL.delete_last()
cirSLL.delete_this(8)
cirSLL.delete_this(77)
cirSLL.print_it()

