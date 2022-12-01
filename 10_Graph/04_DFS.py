class DFS:
	def __init__(self, size):
		self.size = size
		self.color = ['white']*size
		# self.graph = {0:[1], 1:[0,2], 2:[1,3], 3:[2,4,5], 4:[3,5,7], 5:[3,4,6,7], 6:[5,7], 7:[4,5,6]}
		self.graph = {0:[1,2], 1:[2], 2:[3], 3:[1], 4:[3,5], 5:[5]}

	def dfsTraversal(self):
		for i in range(self.size):
			if self.color[i] == 'white':
				self.dfs(i)

	def dfs(self, source):
		stack = []
		stack.append(source)
		self.color[source] = 'gray'

		while stack:
			current = stack.pop()
			print(current, end=' ')
			for i in range(len(self.graph[current])):
				if self.color[self.graph[current][i]] == 'white':
					self.color[self.graph[current][i]] = 'gray'
					stack.append(self.graph[current][i])
			self.color[current] = 'black'

dfs = DFS(6)
dfs.dfsTraversal()