class MinStack:

    def __init__(self):
        self.stack = []
        self.min   = float('inf')
        

    def push(self, val: int) -> None:
        if self.stack == [] or self.min > val:
            self.min = val
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.min:
            del self.stack[-1]
            if self.stack == []:
                self.min = float('inf')
            else:
                self.min = min(self.stack)
        else:
            del self.stack[-1]

    def top(self) -> int:
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

'''
["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
[[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]
'''