#!/usr/bin/env python3

class Graph(object):

    def __init__(self, V):
        self.V = V
        self.adj = {}
        for v in range(self.V):
            self.adj[v] = list()

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def degreee(self, v):
        return len(self.adj[v])

    def maxDegree(self):
        return max([self.degreee(v) for v in range(self.V)])
        
    def avgDegree(self):
        return sum([self.degreee(v) for v in range(self.V)]) / self.V

class BFSPaths(object):

    def __init__(self, g, s):
        self.s = s
        self.g = g
        self.marked = [False] * g.V
        self.parent = [False] * g.V
        self.bfs(s)

    def bfs(self, s):
        queue = [s]
        self.marked[s] = True
        while queue:
            v = queue.pop(0)
            for w in self.g.adj[v]:
                if not self.marked[w]:
                    queue.append(w)
                    self.marked[w] = True
                    self.parent[w] = v

    def hasPathTo(self, v):
        return self.marked[v]

    def pathTo(self, v):
        if not self.hasPathTo(v):
            return None
        path = [v]
        while v != self.s:
            v = self.parent[v]
            path.append(v)
        return path[::-1]