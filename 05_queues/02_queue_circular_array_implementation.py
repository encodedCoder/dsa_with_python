class Queue:
	def __init__(self):
		self.queue = [None]*10
		self.head = 0
		self.tail = 0

	def enqueue(self, data):
		if (self.tail+1) % len(self.queue) != self.head:
			self.tail = (self.tail+1) % len(self.queue)
			self.queue[self.tail] = data
		else:
			print("Queue is full")

	def dequeue(self):
		if self.head == self.tail:
			print("Empty queue")
		else:
			self.head = (self.head+1) % len(self.queue)
			val = self.queue[self.head]
			self.queue[self.head] = None
			return val

	def printQueue(self):
		if self.head == self.tail:
			print("Empty queue")
		else:
			for ele in self.queue:
				print(ele, end=' ')
			print()


queue = Queue()

for i in range(8):
	queue.enqueue(i)

queue.printQueue()

queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()

queue.enqueue(15)
queue.enqueue('18')
queue.enqueue('5')
queue.enqueue('7')

queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()



queue.printQueue()
