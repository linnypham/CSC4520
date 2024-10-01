from collections import deque

def DFS(source,graph):
   DFS = []
   stack = deque()
   visited = set()
   stack.append(source)
   visited.add(source)
   while stack:
      item =stack.pop()
      DFS.append(item)
      for j in graph.get(item,[]):
         if j not in visited:
            stack.append(j)
            visited.add(j)
   return DFS

def DFS_recursive(source, graph, visited=None):
    if visited is None:
        visited = set()
    visited.add(source)
    for neighbor in graph.get(source, []):
        if neighbor not in visited:
            DFS_recursive(neighbor, graph, visited)
    return visited