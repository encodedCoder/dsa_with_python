class Graph:
    def __init__(self, size):
        self.size = size
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0]*size)

    def addEdge(self, v1, v2):
        if v1 == v2:
            return
        self.adjMatrix[v1][v2] = self.adjMatrix[v2][v1] = 1

    def removeEdge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("There is no edge between '{}' and '{}'".format(v1, v2))
            return
        self.adjMatrix[v1][v2] = self.adjMatrix[v2][v1] = 0

    def printGraphMatrix(self):
        print("[")
        for row in self.adjMatrix:
            print("   ", row)
        print("]")


graph = Graph(4)
graph.printGraphMatrix()

graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 2)
graph.addEdge(2, 3)
graph.addEdge(0, 3)
graph.printGraphMatrix()

graph.removeEdge(0, 3)
graph.removeEdge(1, 1)
graph.printGraphMatrix()
