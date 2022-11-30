class QueueNode:
	def __init__(self, data, next = None):
		self.data = data
		self.next = next

class Queue:
	def __init__(self, head = None, tail = None):
		self.head = head
		self.tail = tail

	def enqueue(self, data):
		newNode = QueueNode(data)
		if self.head:
			self.head.next = newNode
			self.head = newNode
		else:
			self.head = self.tail = newNode

	def dequeue(self):
		if self.tail:
			t, t_data = self.tail, self.tail.data
			self.tail = self.tail.next
			del t
			return t_data
		else:
			print("Empty queue")

	def printQueue(self):
		if self.head:
			temp = self.tail
			while temp.next:
				print(temp.data, end = ' ')
				temp = temp.next
			print(temp.data)
		else:
			print("Empty queue")

queue = Queue()
for i in range(10):
	queue.enqueue(i)

queue.printQueue()

queue.dequeue()

queue.printQueue()