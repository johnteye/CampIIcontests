class UnionFind:
    def __init__(self, n):
        self.root = {}
        self.height = {}
        self.group_size = {}

        for i in range(1, n + 1):
            self.root[i] = i
            self.height[i] = 1
            self.group_size[i] = 1

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)

        if rootU != rootV:
            if self.height[rootU] > self.height[rootV]:
                self.root[rootV] = rootU
                self.group_size[rootU] += self.group_size[rootV]
            elif self.height[rootU] < self.height[rootV]:
                self.root[rootU] = rootV
                self.group_size[rootV] += self.group_size[rootU]
            else:
                self.root[rootV] = rootU
                self.height[rootU] += 1
                self.group_size[rootU] += self.group_size[rootV]

    def get_group_size(self, x):
        return self.group_size[self.find(x)]


n, m = map(int, input().split())
uf = UnionFind(n)

for _ in range(m):
    group = list(map(int, input().split()))[1:] 
    for person in group[1:]:
        uf.union(group[0], person)
for i in range(1, n + 1):
    print(uf.get_group_size(i), end=' ')
