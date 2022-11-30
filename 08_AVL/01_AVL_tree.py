class TreeNode:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
		self.height = 1

class AVL_Tree:
	def __init__(self, root=None):
		self.root = root
		pass; pass;

	def buildAVL(self, lst):
		for i in range(len(lst)):
			self.insertIntoAVL(lst[i])

	def insertIntoAVL(self, val):
		if self.root is None:
			self.root = TreeNode(val)
			return

		

	def deleteFromAVL(self):
		pass
		pass


lst = [21,26,30,9,4,14,28,18,15,10,2,3,7]