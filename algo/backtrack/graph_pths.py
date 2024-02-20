"""
Example showing number of paths between given vertices
Usesback trac

1. start at source
2. From source go each connected node
3. Check if adj is the dest if not repeat step 1 and 
   if s == d 
     incrm count and coninue other paths untill all exhausted

"""
class Graph:
    def __init__(self, V):
        #No of verticess
        self.V = V
        self.adj = [[] for i in range(V)]

    def DFSutil(self, v, visited):
        self.visited[v] = True
        print(v)
        for val in self.adj[v]:
            if self.visited[val] != True:
                self.DFSutil(val, visited)

    def addEdge(self, u, v):
        self.adj[u].append(v)



    def pathCount(self, s, d, visited, pcount):
        visited[s] = True
        if s == d:
            pcount[0] += 1
            print(s)
        else:
            ind = 0 
            while ind < len(self.adj[s]):
                if visited[self.adj[s][ind]] == False:
                    print( s, end='')
                    self.pathCount(self.adj[s][ind], d, visited, pcount)
                ind = ind + 1
        visited[s] = False

    def countPaths(self, s, d):
        pcount = [0]
        visited = [False] * self.V
        self.pathCount(s, d, visited, pcount)
        return pcount[0]


if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 3)
    g.addEdge(2, 0)
    g.addEdge(2, 1)
    g.addEdge(1, 3)
    print(g.countPaths(2,3))
