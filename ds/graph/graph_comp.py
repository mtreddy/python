
class Graph:
    def __init__(self, V):
        #No of verticess
        self.V = V
        self.adj = {}
        self.visited = {}

    def DFSutil(self, v, visited):
        self.visited[v] = True
        print(v)
        for val in self.adj[v]:
            if self.visited[val] != True:
                self.DFSutil(val, visited)

    def addEdge(self, u, v):
        if u in self.adj:
            self.adj[u].append(v)
        else:
            self.adj.setdefault(u, [v]);
        if v in self.adj:
            self.adj[v].append(u)
        else:
            self.adj.setdefault(v, [u]);


    def connectedComp(self):
        for ind in self.adj.keys():
            self.visited[ind] = False;
        for ind in self.adj.keys():
            #print(ind)
            if self.visited[ind] == False:
                self.DFSutil(ind, self.visited)
                print("\n")

gr = Graph(10)
gr.addEdge(1,6)
gr.addEdge(2,7)
gr.addEdge(3,8)
gr.addEdge(4,9)
gr.addEdge(2,6)
print(gr.adj)
gr.connectedComp()

