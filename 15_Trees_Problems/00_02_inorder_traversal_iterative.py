# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if root:
            stack = []
            stack.append(root)

            current = root
            while stack:
                if current is None:
                    current = stack.pop()
                    result.append(current.val)
                    if current.right:
                        stack.append(current.right)
                    current = current.right
                else:
                    if current.left:
                        stack.append(current.left)
                    current = current.left

        return result