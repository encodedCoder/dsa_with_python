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
class BinarySearchTree:
    def __init__(self, root = None):
        self.root = root
        pass
    def insertNode(self, val):
        newNode = TreeNode(val)
        if self.root:
            t = self.root
            while True:
                if val < t.val:
                    if t.left:
                        t = t.left
                    else:
                        t.left = newNode
                        break
                else:
                    if t.right:
                        t = t.right
                    else:
                        t.right = newNode
                        break
        else:
            self.root = newNode
    def printPreorder(self, root):
        if root:
            print(root.val, end = ' ')
            self.printPreorder(root.left)
            self.printPreorder(root.right)
    def printPreorderIterative(self, root):
        if root:
            stack = []
            stack.append(root)
            while stack:
                t = stack.pop()
                if t:
                    print(t.val, end=' ')
                    stack.append(t.right)
                    stack.append(t.left)
            print()
    def printInorder(self, root):
        if root:
            self.printInorder(root.left)
            print(root.val, end = ' ')
            self.printInorder(root.right)
    def printInorderIterative(self, root):
        if root:
            stack = []
            while True:
                if root is not None:
                    stack.append(root)
                    root = root.left
                elif stack:
                    root = stack.pop()
                    print(root.val, end = ' ')
                    root = root.right
                else:
                    break
            print()
    def printPostorder(self, root):
        if root:
            self.printPostorder(root.left)
            self.printPostorder(root.right)
            print(root.val, end = ' ')
    def printPostorderIterative(self, root):
        pass
        pass
    def printLevelOrder(self, root):
        if root:
            queue  = Queue()
            result = []
            queue.enQueue(root)
            while queue.front:
                curr = queue.deQueue()
                result.append(curr.val)
                if curr.left:
                    queue.enQueue(curr.left)
                if curr.right:
                    queue.enQueue(curr.right)
            print(result)
            return result
        else:
            return None
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
    def zigzagLevelOrder(self, root):
        if root:
            queue = Queue()
            
            result = []
            currLevel = []

            queue.enQueue(root)
            queue.enQueue('end')
            turnLeft = False
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
                    if turnLeft:
                        currLevel.reverse()
                        turnLeft = False
                    else:
                        turnLeft = True
                    result.append(currLevel)
                    queue.enQueue('end')
                    currLevel = []
            print(result)
            return result
        return None
    def searchNode(self, root, value):
        while root:
            if root.val == value:
                return root
            elif value < root.val :
                root = root.left
            else:
                root = root.right
        else:
            return None
    def deleteNode(self, root, value):
        pass
        pass
    def minElement(self):
        if self.root:
            r = self.root
            while r.left:
                r = r.left
            print(r.val)
    def maxElement(self):
        if self.root:
            r = self.root
            while r.right:
                r = r.right
            print(r.val)
    def countAllNodes(self, root):
        if root:
            leftCount = self.countAllNodes(root.left)
            rightCount = self.countAllNodes(root.right)
            return 1 + leftCount + rightCount
        return 0
    def countLeafNodes(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        else:
            return self.countLeafNodes(root.left) + self.countLeafNodes(root.right)
    def treeMaxDepth(self, root):
        if root is None:
            return 0
        else:
            return 1 + max(self.treeMaxDepth(root.left), self.treeMaxDepth(root.right))

lst = [16,8,24,6,12,18,28,4,6,14,26,30]
lst = [10,5,25,3,2,1,7,30,49,55,50]
lst = [55,38,60,25,45,56,20,26,30,37,36,35,34]
lst = [2,1,33,0,25,40,11,34,7,12,36,13]
lst = [3,2,1,5,4,6,7]
# lst = [2,1,3]
# lst = [1,2,3,4,5]

bst = BinarySearchTree()
for ele in lst:
    bst.insertNode(ele)

# bst.printPreorder(bst.root); print()

bst.printInorder(bst.root); print()

# bst.printPostorder(bst.root); print()

# bst.printPreorderIterative(bst.root)

bst.printInorderIterative(bst.root)

# bst.printPostorderIterative(bst.root)

# bst.printLevelOrder(bst.root)

bst.printLevelOrderPlus(bst.root)

# bst.zigzagLevelOrder(bst.root)

# print(bst.countAllNodes(bst.root))

# print(bst.countLeafNodes(bst.root))

# print(bst.treeMaxDepth(bst.root))

# a = bst.searchNode(bst.root, 8)
# print(a.right.val)

# print()
# bst.minElement()
# bst.maxElement()