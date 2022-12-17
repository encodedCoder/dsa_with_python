# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        result = []

        stack = []
        stack.append(root)
        prev = None
        while stack:
            current = stack[-1]
            if prev = None or prev.left == current or prev.right == current:
                if current.left:
                    stack.append(current.left)
                elif current.right:
                    stack.append(current.right)
                else:
                    result.append(stack.pop())
            elif prev == current.left:
                if current.right:
                    stack.append(current.right)
            else:
                result.append(stack.pop())
            prev = current
        return result