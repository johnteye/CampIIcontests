class UnionFind:
    def __init__(self, n):
        self.root = {}
        self.height = {}

        for i in range(n):
            self.root[i+1] = i+1
            self.height[i] = 1

    def find(self, x):
        if x == self.root[x]:
            return x

        self.root[x] =  self.find(self.root[x])
        return self.root[x]
    

    def union(self, u, v):
        U = self.find(u)
        V = self.find(v)

        if U != V:
            if self.height[U] > self.height[V]:
                self.root[V] = U
                self.height[U] += self.height[V]
            else:
                self.root[U] = V
                self.height[V] += self.height[U]

        else:
            return True
def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        graph = UnionFind(n)
        for _ in range(n):
            u, v = map(int, input().split())
            join = graph.union(u, v)
            if join:
                return print("NO")
        
        count = 0
        for root in graph.root:
            if graph[root] == root:
                count += 1
            if count > 2:
                return print("NO")
            
        return print("YES")
    
solve()
    



