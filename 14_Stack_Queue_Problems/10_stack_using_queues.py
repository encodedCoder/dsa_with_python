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

class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = Queue()
        self.queue2 = Queue()
        
    def push(self, x):
        if self.queue1.rear is None:
            self.queue2.enQueue(x)
        else:
            self.queue1.enQueue(x)

        
    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.queue1.front is not None:
            while self.queue1.front.next:
                self.queue2.enQueue(self.queue1.deQueue())
            tVal = self.queue1.front.data
            self.queue1.deQueue()
            return tVal
        elif self.queue2.front is not None:
            while self.queue2.front.next:
                self.queue1.enQueue(self.queue2.deQueue())
            tVal = self.queue2.front.data
            self.queue2.deQueue()
            return tVal
        else:
            print("Empty Stack")
        
    def top(self):
        """
        Get the top element.
        """
        if self.queue1.front:
            return self.queue1.rear.data
        elif self.queue2.front:
            return self.queue2.rear.data
        else:
            print("Empty Stack")

    def empty(self):
        """
        Returns whether the stack is empty.
        """
        return self.queue1.front is None and self.queue2.front is None
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


# ["MyStack","push","push","top","pop","empty"]
# [[],[1],[2],[],[],[]]
# stack = MyStack()
# stack.push(1)
# stack.push(2)
# print(stack.top())
# print(stack.pop())
# print(stack.empty())

# ["MyStack","push","pop","empty"]
# [[],[1],[],[]]
# stack = MyStack()
# stack.push(1)
# print(stack.pop())
# print(stack.empty())

# ["MyStack","push","empty"]
# [[],[1],[]]
# stack = MyStack()
# stack.push(1)
# print(stack.empty())

# ["MyStack","push","pop","push","top"]
# [[],[1],[],[2],[]]
stack = MyStack()
stack.push(1)
print(stack.pop())
stack.push(2)
print(stack.top())