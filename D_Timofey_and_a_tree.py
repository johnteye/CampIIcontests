from collections import defaultdict

n = int(input())
graph = defaultdict(list)
for _ in range(n-1):
    source, des = map(int, input().split())
    graph[source].append(des)
    graph[des].append(source)

colors = list(map(int, input().split()))
