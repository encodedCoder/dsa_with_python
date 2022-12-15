class StackNode:
	def __init__(self, data, next = None, prev = None):
		self.data = data
		self.next = next
		self.prev = prev
class Stack:
	def __init__(self, top = None, middle = None, nodeCount = 0):
		self.top       = top
		self.middle    = middle
		self.nodeCount = nodeCount

	def push(self, data):
		newNode = StackNode(data)
		if self.nodeCount == 0:
			self.top = self.middle = newNode
		elif self.nodeCount % 2 == 1:
			newNode.next  = self.top
			self.top.prev = newNode
			self.top      = newNode
		else:
			newNode.next  = self.top
			self.top.prev = newNode
			self.top      = newNode
			self.middle   = self.middle.prev
		self.nodeCount += 1

	def pop(self):
		if self.nodeCount == 0:
			print("Empty stack")
			return
		elif self.nodeCount % 2 == 1:
			t = self.top
			self.top = self.top.next
			self.middle = self.middle.next
		else:
			t = self.top
			self.top = self.top.next			
		self.nodeCount -= 1

	def getMiddle(self):
		if self.nodeCount > 0:
			return self.middle

	def deleteMiddle(self):
		if self.nodeCount == 0:
			print("Empty stack")
			return
		elif self.nodeCount == 1:
			self.top = self.middle = None
		elif self.nodeCount == 2:
			self.middle = self.middle.prev
			self.top.next = None
		elif self.nodeCount % 2 == 0:
			t = self.middle
			self.middle = self.middle.prev
			t.next.prev = self.middle
			self.middle.next = t.next
		else:
			t = self.middle
			self.middle = self.middle.next
			t.prev.next = self.middle
			self.middle.prev = t.prev
		self.nodeCount -= 1


	def printStack(self):
		if self.top:
			temp = self.top
			while temp.next:
				print(temp.data, end=' ')
				temp =  temp.next
			print(temp.data)
		else:
			print("Empty stack")


stack = Stack()
for i in range(1,6):
	stack.push(i)

stack.printStack()
print(stack.getMiddle().data)

stack.deleteMiddle()
stack.printStack()
print(stack.getMiddle().data)

stack.deleteMiddle()
stack.printStack()
print(stack.getMiddle().data)

stack.deleteMiddle()
stack.printStack()
print(stack.getMiddle().data)

stack.deleteMiddle()
stack.printStack()
print(stack.getMiddle().data)

try:
	stack.deleteMiddle()
	stack.printStack()
	print(stack.getMiddle().data)
except AttributeError:
	print("Empty stack")
