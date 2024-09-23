from collections import deque
class Graph():
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency = [[]for i in range(vertices)]
    def addEdge(self, vertices, w):
        self.adjacency[vertices].append(w)
        
    def dfs(self, source):
        stack = deque()
        visited = set()
        stack.append(source)
        visited.add(source)
        while stack:
