class Node:
	def __init__(self, val, next=None):
		self.val  = val
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.node_count = 0

	def insert_at_end(self, val):
		new_node = Node(val)
		if self.node_count == 0:
			self.head = self.tail = new_node
		else:
			self.tail.next = new_node
			self.tail = new_node
		self.node_count += 1

	def print_it(self):
		temp = self.head
		while temp:
			print(temp.val, end=', ')
			temp = temp.next



lst = LinkedList()
string_size = int(input("Enter the Size of string: "))
string      = input("Enter the string for LinkedList elements: ")
for i in range(string_size):
	lst.insert_at_end(string[i])
lst.print_it()