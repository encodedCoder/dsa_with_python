'''
We are given a linked list and positions m and n. 
We need to reverse the linked list from position m to n.
Write a program to reverse the list from m to n.
'''

class Node:
    def __init__(self, data, link = None):
        self.data = data
        self.link = link

class LinkedList:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail

    def insert_at_end(self, data):
        newNode = Node(data)
        if self.head:
            self.tail.link = newNode
            self.tail = newNode
        else:
            self.head = self.tail = newNode

    def print_it(self):
        if self.head:
            temp =  self.head
            while temp.link:
                print(temp.data, end = ' ')
                temp = temp.link
            print(temp.data)

    def reverse_N_to_M(self, n, m):
        if m-n:
            if n == 1:
                prev = self.head
                curr = prev.link
                next = curr.link

                for i in range(1, m):
                    curr.link = prev
                    if next:
                        prev, curr, next = curr, next, next.link
                else:
                    if next:
                        self.head.link = curr
                        self.head = prev
                    else:
                        self.head.link = next
                        self.head = curr
            else:
                temp = self.head
                i = 1
                while i <= n-2:
                    i += 1
                    temp = temp.link
                else:
                    prev = temp.link
                    curr = prev.link
                    next = curr.link
                    for i in range(n, m):
                        curr.link = prev
                        prev, curr = curr, next
                        if next:
                            next = next.link
                    else:
                        if curr is next:
                            temp.link.link = next
                            temp.link = prev
                        else:
                            temp.link.link = curr
                            temp.link = prev

# a = LinkedList()
# for i in range(1, 8):
#     a.insert_at_end(i)
# a.print_it()

# a.reverse_N_to_M(3, 7)
# a.print_it()

a = LinkedList()
k, n, m = [int(ele) for ele in input().split()]
eleList = input().split()
for i in range(k):
    a.insert_at_end(eleList[i])
a.reverse_N_to_M(n, m)
a.print_it()