# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class QueueNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class Queue:
    def __init__(self, front=None, rear=None):
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
            t = self.front
            self.front = self.front.next
            return t.data
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
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