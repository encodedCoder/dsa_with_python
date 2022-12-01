from collections import deque

class BFS:
	def __init__(self, size):
		self.size = size
		self.dist = [0]*size
		self.pred = [-1]*size
		self.color = ['white']*size
		self.graph = {0:[1], 1:[0,2], 2:[1,3], 3:[2,4,5], 4:[3,5,7], 5:[3,4,6,7], 6:[5,7], 7:[4,5,6]}

	def bfsTraversal(self, source):
		queue = deque()
		queue.append(source)
		self.dist[source] = 0
		self.color[source] = 'gray'
		while queue:
			current = queue.popleft()
			print(current, end=' ')
			for i in range(len(self.graph[current])):
				if self.color[self.graph[current][i]] == 'white':
					self.dist[self.graph[current][i]]  = self.dist[current] + 1
					self.pred[self.graph[current][i]]  = current
					self.color[self.graph[current][i]] = 'gray'
					queue.append(self.graph[current][i])
			self.color[current] = 'black'
		print()


bfs = BFS(8)
bfs.bfsTraversal(2)
print(bfs.dist)