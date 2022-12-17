# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# def deleteNode(self, root: TreeNode, key: int) -> TreeNode:

class Solution:
    def inorderPredecessor(self, root):
        parent = None
        while root.right:
            parent = root
            root   = root.right
        return root, parent
    def searchNode(self, root, key):
        parent = None
        while root:
            if root.val == key:
                return root, parent
            elif key < root.val:
                parent = root
                root   = root.left
            else:
                parent = root
                root   = root.right
        else:
            return None, None
    def deleteNode(self, root, key):
        # serach the target element
            targetNode, parent = self.searchNode(root, key)
            if targetNode is None:
                return root

        # target node is root node
            if parent is None:
                if targetNode.left is None and targetNode.right is None:        
                    return None
                elif targetNode.left is None:
                    return root.right
                elif targetNode.right is None:
                    return root.left
                else:
                    iOP, parentOfiOP = self.inorderPredecessor(targetNode.left)
                    if parentOfiOP is None:
                        targetNode.val  = iOP.val
                        targetNode.left = targetNode.left.left
                    else:
                        targetNode.val = iOP.val
                        parentOfiOP.right = iOP.left
                return root

        # if target node is leaf node
            if targetNode.left is None and targetNode.right is None:
                if parent.left == targetNode:
                    parent.left = None
                else:
                    parent.right = None
                return root
            
        # if target node is none-leaf node and have only one child
            if targetNode.left is None or targetNode.right is None:
                if targetNode.left is None:
                    if parent.left == targetNode:
                        parent.left = targetNode.right
                    else:
                        parent.right = targetNode.right
                elif targetNode.right is None:
                    if parent.right == targetNode:
                        parent.right = targetNode.left
                    else:
                        parent.left = targetNode.left
                return root

        # target node has two children
            iOP, parentOfiOP = self.inorderPredecessor(targetNode.left)
            if parentOfiOP is None:
                targetNode.val  = iOP.val
                targetNode.left = targetNode.left.left
            else:
                targetNode.val = iOP.val
                parentOfiOP.right = iOP.left
            return root