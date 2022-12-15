class MinStack:
    def __init__(self):
        self.stack = []
        self.min   = 2147483648

    def push(self, val: int) -> None:
        if val < self.min:
            self.stack.append(2*val-self.min)
            self.min = val
        else:
            self.stack.append(val)      

    def pop(self) -> None:
        if self.min > self.stack[-1]:
            self.min = 2*self.min - self.stack[-1]
        del self.stack[-1]

    def top(self) -> int:
        if self.min > self.stack[-1]:
            print(self.min)
            return self.min
        print(self.stack[-1])
        return self.stack[-1]

    def getMin(self) -> int:
        print(self.min)
        return self.min
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

minStack = MinStack()

minStack.push(6)
minStack.push(6)
minStack.push(7)
minStack.top()
minStack.pop()
minStack.getMin()
minStack.pop()
minStack.getMin()
minStack.pop()
minStack.push(7)
minStack.top()
minStack.getMin()
minStack.push(-8)
minStack.top()
minStack.getMin()
minStack.pop()
minStack.getMin()