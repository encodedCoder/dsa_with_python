class Kruskals:
	def __init__(self, size):
		self.size = size
		self.graph = []

	def addEdge(self, u, v, w):
		self.graph.append([u,v,w])

	def kruskals(self):
		result = []
		self.graph = sorted(self.graph,  key=lambda item: item[2])