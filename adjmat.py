class Graph:
  def __init__(self,vertices):
    self.vertices = vertices
    self.size = len(vertices)
    self.vertex_index = {vertex : vindex for vindex , vertex in enumerate(vertices)}
    self.adjmat=[[0] * self.size for _ in range(self.size)]
  def addedge(self,u,v):
    i = self.vertex_index[u]
    j = self.vertex_index[v]
    self.adjmat[i][j]=1 
    self.adjmat[j][i]=1 
  def display(self):
    print("  ","  ".join(self.vertices))
    for i in range(self.size):
      print(self.vertices[i], self.adjmat[i])
      
vertices = ["A","B","C","D","E"]
g1 = Graph(vertices)
g1.addedge("A","B")
g1.addedge("A","C")
g1.addedge("C","D")
g1.addedge("D","E")
