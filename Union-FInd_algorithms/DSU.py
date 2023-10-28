class DSU:
    def __init__(self, n):
        """
            Declare two arrays to hold parent and node information
        """
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def find(self, node):
        """
            Finds the parent of a node
            :param node:
            :return: Parent node
        """
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)

        if u != v:
            if self.rank[u] < self.rank[v]:
                temp = u
                u = v
                v = temp

                self.parent[v] = u
                if self.rank[u] == self.rank[v]:
                    self.rank[u] += 1
