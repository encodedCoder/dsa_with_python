class Node:
	def __init__(self, data, next = None):
		self.data = data
		self.next = next

class LinkedList:
	def __init__(self, head =  None, tail = None):
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
	def union(self, other):
		h1 = self.head
		h2 = other.head
		if h1:

			set_ = set()
			while h1.next:
				set_.add(h1.data)
				h1 =  h1.next
			set_.add(h1.data)
			if h2:
				while h1 and h2:
					if h2.data not in set_:
						h1.next = h2
						h1 = h1.next
						h2 = h2.next
					else:
						h1.next = h2.next
						t = h2
						del t
						if h1:
							h2 = h1.next
	def intersection(self, other):
		h1 = self.head
		h2 = other.head

		if h1 and h2:
			set_ = set()
			while h1.next:
				set_.add(h1.data)
				h1 = h1.next
			else:
				set_.add(h1.data)
			while h2 and h2.data not in set_:
				h2 = h2.next
			else:
				if h2:
					self.head = h1 = h2
					h2 = h2.next		
				while h2:
					if h2.data in set_:
						h1.next = h2
						h1 = h1.next
					h2 = h2.next
				if h1:
					h1.next = None

if __name__ == '__main__':
	lst1 = [6,4,2,8,10]
	lst2 = [2,1,3,4,5]

	lst1 = [10,15,4,20]
	lst2 = [8,4,2,10]

	a = LinkedList()
	b = LinkedList()

	for i in range(len(lst1)):
		a.insert_at_end(lst1[i])
	for i in range(len(lst2)):
		b.insert_at_end(lst2[i])

	a.print_it()
	b.print_it()

	a.union(b)
	a.print_it()

	# a.intersection(b)
	# a.print_it()