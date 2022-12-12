'''
Write a function that takes two lists, each of which is sorted in increasing order,
and merges the two together into one list which is in increasing order. 
Function should return the new list. 
The new list should be made by splicing together the nodes of the first two lists.
'''
class Node:
	def __init__(self, data, next=None):
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
				print(temp.data, end=' ')
				temp = temp.next
			print(temp.data)

def merge_two_sorted_lists(head1, head2, lst1_len = 0, lst2_len = 0):
	c = LinkedList()
	while head1 and head2:
		if head1.data < head2.data:
			data  = head1.data
			head1 = head1.next
		else:
			data = head2.data
			head2 = head2.next
		c.insert_at_end(data)

	while head1:
		data  = head1.data
		head1 = head1.next
		c.insert_at_end(data)

	while head2:
		data = head2.data
		head2 = head2.next
		c.insert_at_end(data)

	c.print_it()
	return c


a = LinkedList()
for i in range(1, 11, 2):
	a.insert_at_end(i)
a.print_it()

b = LinkedList()
for i in range(2, 14, 3):
	b.insert_at_end(i)
b.print_it()

c = merge_two_sorted_lists(a.head, b.head)
c.print_it()


# lst1_len, lst2_len = [int(ele) for ele in input().split()]
# lst1 = [int(ele) for ele in input().split()]
# lst2 = [int(ele) for ele in input().split()]

# a = LinkedList()
# b = LinkedList()

# for i in range(lst1_len):
# 	a.insert_at_end(lst1[i])

# for i in range(lst2_len):
# 	b.insert_at_end(lst2[i])

# merge_two_sorted_lists(a.head, b.head)