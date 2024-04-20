class UnionFind:
    def __init__(self, roots):
        self.root = {}
        self.size = {}

        for i in roots:
            self.root[i] = i
            self.size[i] = 1

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, u, v):
        U = self.find(u)
        V = self.find(v)

        if U != V:
            if self.size[U] > self.size[V]:
                self.root[V] = U
                self.size[U] += self.size[V]

            else:
                self.root[U] = V
                self.size[V] += self.size[U]

n ,m = map(int,input().split())
count = 0
langs = []
roots = set()
for i in range(n):
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        count += 1
    else:
        langs.append(arr[1:])
        roots.update(arr[1:])

graph = UnionFind(roots)

for lang in langs:
    for i in range(len(lang)):
        for j in range(i+1, len(lang)):
            graph.union(lang[i], lang[j])

for node in graph.root:
    if graph.root[node] == node:
        count += 1

print(count-1 if langs else count)