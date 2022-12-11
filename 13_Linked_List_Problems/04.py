class Node:
	def __init__(self, info, next = None):
		self.info = info
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.node_count = 0
	def insert_at_end(self, info):
		new_node = Node(info)
		if self.head:
			self.tail.next = new_node
			self.tail = new_node
		else:
			self.head = self.tail = new_node
		self.node_count += 1
	def print_it(self):
		if self.node_count == 0:
			print("Empty List")
		else:
			temp_head = self.head
			while temp_head:
				print(temp_head.info, end=' ')
				temp_head = temp_head.next
			print()
	def swap_kth_and_prev_from_end(self, list_len, k):
		if k >= 2:
			temp = self.head

			camparison_val = list_len-k
			for i in range(camparison_val):
				temp = temp.next

			temp.info, temp.next.info = temp.next.info, temp.info


linked_list = LinkedList()
lst_1 = input().split()
lst_2 = input().split()
for i in range(len(lst_2)):
	linked_list.insert_at_end(lst_2[i])

linked_list.swap_kth_and_prev_from_end(int(lst_1[0]), int(lst_1[1]))
linked_list.print_it()