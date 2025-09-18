class Graph:
    def __init__(self):
        self.adjlist = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjlist:
            self.adjlist[vertex] = []

    def add_edge(self, u, v):
        if u not in self.adjlist:
            self.add_vertex(u)
        if v not in self.adjlist:
            self.add_vertex(v)
        self.adjlist[u].append(v)
        self.adjlist[v].append(u)

    def display(self):
        for vertex in self.adjlist:
            print(f"{vertex} : {self.adjlist[vertex]}")

g = Graph()

n = int(input())
for _ in range(n):
    u, v = input().split()
    g.add_edge(u, v)
g.display()
