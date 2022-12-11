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
    def delete_n_skip_m(self, n, m):
        temp_head = self.head
        while temp_head:
            # skipping part --> skip m nodes
            i = m
            while i-1 and temp_head:
                temp_head = temp_head.next
                i -= 1

            lower_end = temp_head

            # deletion_part --> delete n nodes
            j = n
            if temp_head:
                temp_head = temp_head.next
            while j and temp_head:
                temp = temp_head
                temp_head = temp_head.next
                del temp
                j -= 1

            if lower_end:
                lower_end.next = temp_head


N_n_m = input().split()
lst = input().split()

# N_n_m = [7,1,2]
# lst   = [1,2,3,4,5,6,7]

# N_n_m = [8,2,2]
# lst   = [1,2,3,4,5,6,7,8]

# N_n_m = [11, 3, 3]
# lst   = [1,2,3,4,5,6,7,8,9,10,11]

linkedList = LinkedList()
for i in range(int(N_n_m[0])):
    linkedList.insert_at_end(lst[i])

linkedList.print_it()
linkedList.delete_n_skip_m(int(N_n_m[1]), int(N_n_m[2]))
linkedList.print_it()