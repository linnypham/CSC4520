from collections import deque
def BFS(source,graph):
   BFS = []
   q = deque()
   visited = set()
   q.append(source)
   visited.add(source)
   while q:
      item =q.popleft()
      BFS.append(item)
      for j in graph.get(item,[]):
         if j not in visited:
            q.append(j)
            visited.add(j)
   return BFS