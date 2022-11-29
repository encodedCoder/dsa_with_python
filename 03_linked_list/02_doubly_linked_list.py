class Node():
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.node_count = 0

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = new_node
        self.node_count += 1

    def insert_at_end(self, data):
        new_node = Node(data)
        temp_head = self.head
        if temp_head:
            while temp_head.next:
                temp_head = temp_head.next
            new_node.prev = temp_head
            temp_head.next = new_node
        else:
            self.head = new_node
        self.node_count += 1


    def insert_after(self, data, target_data):
        new_node = Node(data)
        if self.head:
            temp_head = self.head
            while temp_head.data != target_data and temp_head.next:
                temp_head = temp_head.next
            new_node.prev = temp_head
            new_node.next = temp_head.next
            temp_head.next = new_node
        else:
            self.head = new_node
        self.node_count += 1


    def delete_first(self):
        if self.node_count == 0:
            print("Empty List")
        elif self.node_count == 1:
            temp = self.head
            self.head = None
            del temp
            self.node_count -= 1
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            del temp
            self.node_count -= 1

    def delete_last(self):
        if self.node_count == 0:
            print("Empty List")
        elif self.node_count == 1:
            temp = self.head
            self.head = None
            del temp
            self.node_count -= 1
        else:
            temp_head = self.head
            while temp_head.next.next:
                temp_head = temp_head.next
            temp = temp_head.next
            temp_head.next = None
            del temp
            self.node_count -= 1

    def delete_this(self, target_data):
        if self.node_count == 0:
            print("Empty List")
            return
        elif self.node_count == 1:
            if self.head.data == target_data:
                temp = self.head
                self.head = None
                del temp
                self.node_count -= 1
            else:
                print("Element not present")
            return
        else:
            temp_head = self.head
            while temp_head.data != target_data and temp_head.next:
                temp_head = temp_head.next
            # if target node is first node
            if temp_head.prev == None and temp_head.data == target_data:
                temp = temp_head
                self.head = temp_head.next
                self.head.prev = None
                del temp
                self.node_count -= 1
                return
            # if target node is last node
            elif temp_head.next == None and temp_head.data == target_data:
                temp = temp_head
                temp_head.prev.next = None
                del temp
                self.node_count -= 1
                return
            # if target node is inbetween node
            elif temp_head.data == target_data:
                temp = temp_head
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                del temp
                self.node_count -= 1        
        print("Element not present.")


    def print_it(self):
        temp_head = self.head
        if temp_head:
            while temp_head:
                print(temp_head.data, end = ', ')
                temp_head = temp_head.next
            print("\nTotal Nodes:", self.node_count)
        else:
            print("Empty List")
       
dbl_lst = DoublyLinkedList()

dbl_lst.insert_at_end(7)
dbl_lst.insert_at_end(9)
dbl_lst.insert_at_beginning(5)
dbl_lst.insert_at_beginning(2)
dbl_lst.insert_at_end(3)
dbl_lst.insert_after(11, 9)
dbl_lst.insert_after(8, 200)
dbl_lst.insert_after(64, 2)
dbl_lst.print_it()
# dbl_lst.delete_first()
# dbl_lst.delete_last()
dbl_lst.delete_this(2)
# dbl_lst.delete_this(200)
dbl_lst.delete_this(9)
dbl_lst.print_it()