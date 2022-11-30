class QueueNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Queue:
    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear  = rear
    def enQueue(self, val):
        newNode = QueueNode(val)
        if self.front:
            self.rear.next = newNode
            self.rear = newNode
        else:
            self.front = self.rear = newNode
    def deQueue(self):
        if self.front:
            t = self.front
            self.front = self.front.next
            return t.val

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val  = val
        self.left  = left
        self.right = right
class ExpressionTree:
    def __init__(self, root = None):
        self.root = root
        pass
    def createExpressionTree(self, strr):
        #str: postfix string of the arithmetic expression
        operators = ['/','*','+','-']
        operandss = [0,1,2,3,4,5,6,7,8,9]
        operands  = ['0','1','2','3','4','5','6','7','8','9']

        stack = []
        for ele in strr:
            if ele in operands:
                stack.append(int(ele))
            elif ele in operators:
                parent = TreeNode(ele)
                rightChild = stack.pop()
                leftChild  = stack.pop()

                if rightChild in operandss:
                    parent.right = TreeNode(rightChild)
                else:
                    parent.right = rightChild

                if leftChild in operandss:
                    parent.left = TreeNode(leftChild)
                else:
                    parent.left = leftChild

                stack.append(parent)
        self.root = parent
    def printLevelOrderPlus(self, root):
        if root:
            queue = Queue()
            
            result = []
            currLevel = []
           
            queue.enQueue(root)
            queue.enQueue('end')
            while True:
                curr = queue.deQueue()
                if curr != 'end':
                    currLevel.append(curr.val)
                    if curr.left:
                        queue.enQueue(curr.left)
                    if curr.right:
                        queue.enQueue(curr.right)
                elif currLevel == []:
                    break
                else:
                    result.append(currLevel)
                    queue.enQueue('end')
                    currLevel = []
            print(result)
            return result
        return None
    def calculate(self, leftVal, rightVal, operator):
        if operator == '/':
            return leftVal / rightVal
        elif operator == '*':
            return leftVal * rightVal
        elif operator == '+':
            return leftVal + rightVal
        elif operator == '-':
            return leftVal - rightVal
    def evaluateExpressionTree(self, root):
        operators = ['/','*','+','-']
        if root.left.val in operators:
            leftVal = self.evaluateExpressionTree(root.left)
        else:
            leftVal = root.left.val

        if root.right.val in operators:
            rightVal = self.evaluateExpressionTree(root.right)
        else:
            rightVal = root.right.val

        return self.calculate(leftVal, rightVal, root.val)

postfix = "12+345+**"
postfix = "23+456+**"
# postfix = "12+"
# postfix = "23*456-8/*+"
# postfix = "23*456-*+"

et = ExpressionTree()
et.createExpressionTree(postfix)
et.printLevelOrderPlus(et.root)
print(et.evaluateExpressionTree(et.root))