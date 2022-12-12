class Node:
	def __init__(self, data, next = None, prev = None):
		self.data = data
		self.next = next
		self.prev = prev

class EfficientDLL:
	def __init__(self):
		self.head = None
		self.tail = None

	def insertAtEnd(self, data):
		newNode = Node(data)
		if self.head:
			