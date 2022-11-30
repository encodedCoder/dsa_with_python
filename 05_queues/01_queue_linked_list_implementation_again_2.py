class QueueNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class Queue:
    def __init__(self, front = None, rear = None):
        self.front = front
        self.rear  = rear
    def enQueue(self, data):
        newNode = QueueNode(data)
        if self.front:
            self.rear.next = newNode
            self.rear = newNode
        else:
            self.front = self.rear = newNode
    def deQueue(self):
        if self.front:
            temp = self.front
            tVal = self.front.data
            self.front = self.front.next
            del temp
            return tVal
    def printQueue(self):
        if self.front:
            temp = self.front
            while temp.next:
                print(temp.data, end = ' ')
                temp = temp.next
            print(temp.data)