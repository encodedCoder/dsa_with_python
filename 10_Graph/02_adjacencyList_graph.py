class GraphNode:
	def __init__(self, val, next=None):
		self.val = val
		self.next = next

class Graph:
	def __init__(self, size):
		self.size = size
		self.graph = [None] * size

	def addEdge(self, v1, v2):
		if v1 == v2:
			print("Both Same vertices")
			return
		self.graph[v1] = GraphNode(v2, self.graph[v1])
		self.graph[v2] = GraphNode(v1, self.graph[v2])

	def printGraph(self):
		for i in range(self.size):
			print(i, end='-->')
			root = self.graph[i]
			while root:
				print(root.val, end='-->')
				root = root.next
			print(root)

graph = Graph(4)
graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 2)
graph.addEdge(2, 3)
graph.printGraph()