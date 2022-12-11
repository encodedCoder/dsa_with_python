class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self, head = None):
        self.head = head
        self.tail = head
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = self.tail = new_node
    def print_it(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()
    def alternatingSplit(self):
        head1 = temp1 = self.head
        head2 = temp2 = temp1.next
        while temp1.next and temp2.next:
            temp1.next = temp2.next
            temp1 = temp2.next
            
            temp2.next = temp1.next
            temp2 = temp1.next
        
        if temp1:
            temp1.next = None
        else:
            temp2.next = None
            
        return LinkedList(head1), LinkedList(head2)
    
list_length = int(input())
lst = input().split()

# list_length = 2
# lst = [1,2,3,4,5,6,7]

linkedList = LinkedList()
for i in range(list_length):
    linkedList.insert_at_end(lst[i])
    
h1, h2 = linkedList.alternatingSplit()

h1.print_it()
h2.print_it()