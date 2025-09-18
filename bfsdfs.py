from collections import deque
class Graph:
  def __init__(self):
    self.adj_list={}
  def addvertex(self,vertex):
    if vertex not in self.adj_list:
      self.adj_list[vertex]=[]
  def addedges(self,u,v):
    if u not in self.adj_list:
      self.addvertex(u)
    if v not in self.adj_list:
      self.addvertex(v)
    self.adj_list[u].append(v)
    self.adj_list[v].append(u)
  def display(self):
    for i in self.adj_list:
      print(f"{i}:{self.adj_list[i]}")
  def bfs(self,start):
    visited=set()
    q=deque()
    q.append(start)
    visited.add(start)
    while len(q)!=0:
      vertex=q.popleft()
      print(vertex,end=" ")
      for i in self.adj_list[vertex]:
        if i not in visited:
          q.append(i)
          visited.add(i)
  def dfs(self,start,visited=None):
    if visited is None:
      visited=set()
    visited.add(start)
    print(start,end=" ")
    for i in self.adj_list[start]:
      if i not in visited:
        self.dfs(i,visited)
  
g = Graph()

n = int(input())
for _ in range(n):
    u, v = input().split()
    g.addedges(u, v)
g.display()

print("BFS:")
g.bfs("A")
print("\nDFS:")
g.dfs("A")
