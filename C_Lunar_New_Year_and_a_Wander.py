
from collections import defaultdict
import heapq
n , e = map(int, input().split())

graph = defaultdict(list)

for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

heap = []
heapq.heapify(heap)
res = []
visited = set()
heap.append(1)

while heap:
    curr = heapq.heappop(heap)
    if curr in visited:
        continue
    res.append(curr)
    visited.add(curr)

    for n in graph[curr]:
        if n not in visited:
            heapq.heappush(heap, n)

print(*res)



